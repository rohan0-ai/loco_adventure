from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from api.services import get_place_details
from api.serializers import PlaceDetailSerializer



class PlaceDetailAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, xid):

        place = get_place_details(xid)

        serializer = PlaceDetailSerializer(place)

        return Response(serializer.data)