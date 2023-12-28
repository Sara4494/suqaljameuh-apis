from users.apis.serializers import AdminSerializer
from rest_framework import decorators, status, permissions
from rest_framework.response import Response



@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAdminUser])
def create_admin (request)  :

    try : 
        username = request.data.get('username')

        if not username :
            return Response({'message':"username field cannot be empty"},status=status.HTTP_400_BAD_REQUEST)
        
        serializer = AdminSerializer(data=request.data)

        if serializer.is_valid() :
            
            serializer.save()
            serializer.set_username(username)
            
            tokens = serializer.get_jwt_tokens()
            
            return Response(tokens,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as e :
        return Response({"message":f"an error accured {e}"},status=status.HTTP_400_BAD_REQUEST)
