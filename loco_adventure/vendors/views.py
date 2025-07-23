from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from core.forms import CustomUserCreationForm

# Vendor Registration
def vendor_registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'V'
            user.save()
            # Create Vendor profile linked to user
            from .models import Vendor
            Vendor.objects.create(user=user, business_name=user.username)
            messages.success(request, 'Vendor account created successfully. Please log in.')
            return redirect('vendors:vendor-login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm(initial={'user_type': 'V'})
    return render(request, 'vendors/manager.html', {'form': form})

# Vendor Login
def vendor_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.user_type == 'V':
            login(request, user)
            return redirect('vendors:vendor-dashboard')
        else:
            messages.error(request, 'Invalid credentials or not a vendor.')
    return render(request, 'vendors/login.html')

# Vendor Logout
def vendor_logout(request):
    logout(request)
    return redirect('home')

from django.contrib.auth.decorators import login_required
from adventures.models import Adventure

# Vendor Dashboard
@login_required
def vendor_dashboard(request):
    user = request.user
    try:
        vendor = user.vendor
    except Exception:
        vendor = None

    if vendor is None:
        # Redirect or show error if user is not a vendor
        return redirect('home')

    if request.method == 'POST':
        # Handle new adventure creation
        from core.forms import AdventureForm
        form = AdventureForm(request.POST, request.FILES)
        if form.is_valid():
            adventure = form.save(commit=False)
            adventure.vendor = vendor
            adventure.save()
            return redirect('vendors:vendor-dashboard')
        else:
            # Pass form with errors to template
            adventures = vendor.adventure_set.all()
            return render(request, 'vendors/managerdash.html', {'adventures': adventures, 'vendor': vendor, 'form': form})

    adventures = vendor.adventure_set.all()
    from core.forms import AdventureForm
    form = AdventureForm()
    return render(request, 'vendors/managerdash.html', {'adventures': adventures, 'vendor': vendor, 'form': form})

# Edit Adventure
from core.forms import AdventureForm

@login_required
def edit_adventure(request, adventure_id):
    user = request.user
    try:
        vendor = user.vendor
    except Exception:
        vendor = None

    if vendor is None:
        return redirect('home')

    adventure = get_object_or_404(Adventure, pk=adventure_id, vendor=vendor)

    if request.method == 'POST':
        form = AdventureForm(request.POST, request.FILES, instance=adventure)
        if form.is_valid():
            form.save()
            return redirect('vendors:vendor-dashboard')
    else:
        form = AdventureForm(instance=adventure)

    return render(request, 'vendors/edit_adventure.html', {'form': form, 'adventure': adventure})
