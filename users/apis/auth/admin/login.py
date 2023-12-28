from rest_framework import decorators, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User

@decorators.api_view(['POST'])
def admin_login (request)  :

    try :

        email = request.data.get('email')
        password = request.data.get('password')

        
        if not email :
            return Response({'message':'email cannot be empty'},status=status.HTTP_400_BAD_REQUEST)
        
        if not password :
            return Response({'message':'password cannot be empty'},status=status.HTTP_400_BAD_REQUEST)
        
        users = User.objects.filter(email=email,is_staff=True)

        if not users.exists() :
            return Response({'message':'Invalid Email'},status=status.HTTP_400_BAD_REQUEST)
            
        user = users.first()

        if not user.check_password(password) : 
            return Response({'message':'Invalid Password'},status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user)

        jwt_tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return Response(jwt_tokens,status=status.HTTP_200_OK)
    except Exception as e :
        return Response({'message':f"an error accured : {e}"},status=status.HTTP_400_BAD_REQUEST)
        