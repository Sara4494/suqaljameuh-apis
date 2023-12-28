from rest_framework import decorators, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User


def generate_token(user):
    refresh = RefreshToken.for_user(user)

    jwt_tokens = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return jwt_tokens


@decorators.api_view(['POST'])
def login(request):

    try:

        email = request.data.get('email')
        password = request.data.get('password')

        if not email:
            return Response({'message': 'email cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)

        if not password:
            return Response({'message': 'password cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)

        users = User.objects.filter(email=email, is_staff=False)

        if not users.exists():
            return Response({'message': 'Invalid Email'}, status=status.HTTP_400_BAD_REQUEST)

        user = users.first()

        if not user.check_password(password):
            return Response({'message': 'Invalid Password'}, status=status.HTTP_400_BAD_REQUEST)

        jwt_tokens = generate_token(user)

        return Response({
            "data": jwt_tokens
        }, status=status.HTTP_200_OK)

    except Exception as error:
        return Response({'message': f'An error occurred : {error}'}, status=status.HTTP_400_BAD_REQUEST)
