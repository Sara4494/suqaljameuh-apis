from rest_framework.decorators import api_view, permission_classes
from ...models import Profile
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def check_user (request) :

    try :
        username = request.POST["username"]

        if username :
            user = Profile.objects.filter(username=username)
            
            if user.exists():
                return Response({'message':'this username not avaliable '},status=status.HTTP_200_OK)
            else : 
                return Response({'message':'this username is avaliable'},status=status.HTTP_200_OK)
        else :
            return Response({'message':'username can not be empty'},status=status.HTTP_200_OK)

    except Exception as error :
        return Response({'messsage':f'an errror occurred : {error}'},status=status.HTTP_400_BAD_REQUEST)