from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.services import search_nearby_places
from api.serializers import NearbyResponseSerializer


class NearbyPlacesView(APIView):
    def get(self, request):
        try:
            lat = request.query_params.get("lat")
            lng = request.query_params.get("lng")

            if not lat or not lng:
                return Response(
                    {"error": "lat and lng are required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Optional query parameters
            radius = int(request.query_params.get("radius", 5000))
            limit = int(request.query_params.get("limit", 10))

            places = search_nearby_places(
                lat=float(lat),
                lon=float(lng),
                radius=radius,
                limit=limit,
            )

            response_data = {
                "count": len(places),
                "results": places,
            }

            serializer = NearbyResponseSerializer(response_data)

            return Response(serializer.data)

        except ValueError:
            return Response(
                {
                    "error": "lat, lng, radius and limit must be valid numbers."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )