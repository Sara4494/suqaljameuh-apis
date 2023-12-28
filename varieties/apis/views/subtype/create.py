from varieties.models import *
from varieties.apis.serializers import *
from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes
@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def create_subtype(request):
    try:
        name = request.data.get('name')
        type = request.data.get('type')

        try:
            type_model = Type.objects.get(name=type)
        except Type.DoesNotExist:
            return Response({
                "message": "this type doesn't exists"
            }, status=status.HTTP_404_NOT_FOUND)

        if SubType.objects.filter(name=name, type=type_model).exists():
            return Response({'error': _('This name is already registered at the SubType.')}, status=status.HTTP_400_BAD_REQUEST)
    
        try:
            SubType.objects.create(
                name = name,
                type = type_model
            )
            return Response({
                "message": "Subtype created successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                "message": "an error occurred while creating the subtype"
            }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
 
 

 