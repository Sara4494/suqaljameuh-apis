from rest_framework.response import Response
from rest_framework import status, permissions, decorators
from settings.apis.serializers import PageSerializer

@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAdminUser])
def CreatePage (request) : 

    try : 
        serializer = PageSerializer(data=request.data)

        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as error : 
        return Response({'message':f'An error accured : {error}'},status=status.HTTP_400_BAD_REQUEST)