from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Homepage
def index(request):
    return render(request, 'core/index.html')

from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

# User Registration
def user_registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'C'
            user.phone = ''  # default empty phone
            user.profile_pic = None  # default no profile pic
            user.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('user-dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/user.html', {'form': form})

# User Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.user_type == 'C':
            login(request, user)
            return redirect('user-dashboard')
        else:
            messages.error(request, 'Invalid credentials or not a customer.')
    return render(request, 'users/login.html')

# User Logout
def user_logout(request):
    logout(request)
    return redirect('home')

from adventures.models import Adventure
from django.contrib.auth.decorators import login_required
from django.db.models import F, FloatField
from django.db.models.functions import ACos, Cos, Radians, Sin

def get_initials(user):
    if not user.is_authenticated:
        return None

    if user.first_name and user.last_name:
        return f"{user.first_name[0].upper()}{user.last_name[0].upper()}"
    elif user.first_name:
        return user.first_name[0].upper()
    elif user.last_name:
        return user.last_name[0].upper()
    else:
        return user.username[:2].upper()

from .forms import AdventureFilterForm

def user_dashboard(request):
    user = request.user
    user_lat = request.GET.get('latitude')
    user_lon = request.GET.get('longitude')

    form = AdventureFilterForm(request.GET or None)

    adventures = Adventure.objects.filter(vendor__verified=True)

    if form.is_valid():
        category = form.cleaned_data.get('category')
        search = form.cleaned_data.get('search')

        if category:
            adventures = adventures.filter(adventure_type=category)

        if search:
            adventures = adventures.filter(title__icontains=search)

    if user_lat and user_lon:
        try:
            user_lat = float(user_lat)
            user_lon = float(user_lon)
            adventures = adventures.annotate(
                distance=6371 * ACos(
                    Cos(Radians(user_lat)) * Cos(Radians(F('latitude'))) *
                    Cos(Radians(F('longitude')) - Radians(user_lon)) +
                    Sin(Radians(user_lat)) * Sin(Radians(F('latitude')))
                )
            , output_field=FloatField()).order_by('distance')
        except (ValueError, TypeError):
            pass

    featured_adventures = adventures[:3]

    # Add truncated_description attribute to each adventure
    for adventure in featured_adventures:
        if adventure.description and len(adventure.description) > 100:
            adventure.truncated_description = adventure.description[:100] + "..."
        else:
            adventure.truncated_description = adventure.description or "Exciting adventure awaits."

    initials = get_initials(user)
    context = {
        'user': user,
        'is_authenticated': user.is_authenticated,
        'featured_adventures': featured_adventures,
        'initials': initials,
        'form': form,
    }
    return render(request, 'core/usermain.html', context)

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator

# Booking Page
import datetime

def booking(request, adventure_id):
    adventure = get_object_or_404(Adventure, pk=adventure_id)
    quantity = 1
    total_amount = adventure.price * quantity
    current_date = datetime.date.today().isoformat()  # Format date as YYYY-MM-DD string
    context = {
        'adventure': adventure,
        'quantity': quantity,
        'total_amount': total_amount,
        'current_date': current_date,
    }
    return render(request, 'core/booking.html', context)

def load_more_adventures(request):
    user_lat = request.GET.get('latitude')
    user_lon = request.GET.get('longitude')
    category = request.GET.get('category')
    search = request.GET.get('search')
    page = request.GET.get('page', 1)
    adventures_per_page = 3

    adventures = Adventure.objects.filter(vendor__verified=True)

    if category:
        adventures = adventures.filter(adventure_type=category)

    if search:
        adventures = adventures.filter(title__icontains=search)

    if user_lat and user_lon:
        try:
            user_lat = float(user_lat)
            user_lon = float(user_lon)
            adventures = adventures.annotate(
                distance=6371 * ACos(
                    Cos(Radians(user_lat)) * Cos(Radians(F('latitude'))) *
                    Cos(Radians(F('longitude')) - Radians(user_lon)) +
                    Sin(Radians(user_lat)) * Sin(Radians(F('latitude')))
                )
            , output_field=FloatField()).order_by('distance')
        except (ValueError, TypeError):
            pass

    paginator = Paginator(adventures, adventures_per_page)
    try:
        adventures_page = paginator.page(page)
    except:
        adventures_page = []

    adventures_list = []
    for adventure in adventures_page:
        adventures_list.append({
            'id': adventure.id,
            'title': adventure.title,
            'image_url': adventure.image.url if adventure.image else '/static/Images/default.jpg',
            'vendor_rating': getattr(adventure.vendor, 'rating', '4.5'),
            'address': adventure.address if adventure.address else '',
            'description': (adventure.description[:100] + '...') if adventure.description and len(adventure.description) > 100 else (adventure.description if adventure.description else 'Exciting adventure awaits.'),
            'price': adventure.price,
            'duration': 'per person',
            'online_booking': adventure.online_booking,
        })

    return JsonResponse({
        'adventures': adventures_list,
        'has_next': adventures_page.has_next() if adventures_page else False,
    })
