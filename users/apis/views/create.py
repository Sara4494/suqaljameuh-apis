from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from users.models import User
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
