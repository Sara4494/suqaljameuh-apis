from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from users.models import User, Rating
from users.apis.serializers import UserSerializer
from rest_framework import status,permissions
from rest_framework import status
from django.shortcuts import get_object_or_404
 
from django.db import transaction

@api_view(['POST'])
@permission_classes([permissions.IsAdminUser]) 
def create(request):
    data = request.data
    try:
        with transaction.atomic():
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "User created successfully"
                }, status=status.HTTP_200_OK)
            return Response({
                "message": f'an error occurred {serializer.errors}'
            }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            "message": f"an error occurred when creating the user {e}"
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST",])
@permission_classes([permissions.IsAuthenticated])
def rate_user(request, user_id):
    data = request.data
    from_user = request.user

    if not data:
        return Response({
            "message": "You must provide the needed data to rate this user"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        to_user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({
            "message": "The user you're trying to rate isn't available on our site"
        }, status=status.HTTP_404_NOT_FOUND)

    rating = data.get('rating')

    rating_exists = Rating.objects.filter(from_user=from_user, to_user=to_user).exists()

    if rating_exists:
        return Response({
            "message": "You already have rated this user one time before"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        Rating.objects.create(to_user=to_user, from_user=from_user, rate=rating)
        
        ratings = to_user.user_ratings.all()
        to_user.ratings_count = len(ratings)
        total = 0

        for i in ratings:
            total = i.rate
        
        to_user.rate = total / len(ratings)
        to_user.save()
        return Response({
            "data": f"You have rated {to_user.full_name}"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": f"An error occurred while creating the review {e}"
        }, status=status.HTTP_400_BAD_REQUEST)