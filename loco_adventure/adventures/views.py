from django.shortcuts import render, get_object_or_404
from .models import Adventure
from django.db.models import F, FloatField
from django.db.models.functions import ACos, Cos, Radians, Sin

def adventure_list(request):
    user_lat = request.GET.get('latitude')
    user_lon = request.GET.get('longitude')
    adventures = Adventure.objects.all()

    if user_lat and user_lon:
        try:
            user_lat = float(user_lat)
            user_lon = float(user_lon)
            # Haversine formula to calculate distance in km
            adventures = adventures.annotate(
                distance=6371 * ACos(
                    Cos(Radians(user_lat)) * Cos(Radians(F('latitude'))) *
                    Cos(Radians(F('longitude')) - Radians(user_lon)) +
                    Sin(Radians(user_lat)) * Sin(Radians(F('latitude')))
                )
            , output_field=FloatField()).order_by('distance')
        except (ValueError, TypeError):
            pass

    return render(request, 'adventures/adventure_list.html', {'adventures': adventures})

def adventure_detail(request, pk):
    adventure = get_object_or_404(Adventure, pk=pk)
    return render(request, 'adventures/adventure_detail.html', {'adventure': adventure})

def place_detail(request, xid):
    return render(
        request,
        "core/place_detail.html",
        {
            "xid": xid,
        },
    )
