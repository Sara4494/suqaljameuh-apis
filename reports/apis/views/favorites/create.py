from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from reports.models import Favorites
from reports.apis.serializers import *
from Ad.models import Ad
from django.core import exceptions
 

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_favorite(request, ad_id):
    try:
        ad = Ad.objects.get(pk=ad_id)
    except exceptions.ObjectDoesNotExist:
        return Response({
            "message": "Ad not found"
        }, status=status.HTTP_404_NOT_FOUND)
    
    already_in_favorite = Favorites.objects.filter(ad=ad).exists()
    if already_in_favorite:
        return Response({
            "message": "You already have this ad in your favorites"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        Favorites.objects.create(
            ad = ad,
            user = request.user
        )
        return Response({
            "message": "we added this add to your favorites successfully"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({'message': 'An error occurred', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)