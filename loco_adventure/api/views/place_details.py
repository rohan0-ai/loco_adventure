from rest_framework.views import APIView
from rest_framework.response import Response

from api.providers import get_place_details
from serializers import PlaceDetailSerializer



class PlaceDetailAPIView(APIView):

    def get(self, request, xid):

        place = get_place_details(xid)

        serializer = PlaceDetailSerializer(place)

        return Response(serializer.data)