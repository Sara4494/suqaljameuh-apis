from users.models import User
from rest_framework.response import Response
from rest_framework import decorators, status, permissions
import datetime
from ..calc_increase import calc_increase_percentage


@decorators.api_view(["GET"])
@decorators.permission_classes([permissions.IsAdminUser])
def GetWeklyUsers (request) : 
    try : 
        
        to = datetime.datetime.now() - datetime.timedelta(weeks=1)
        from_ = to - datetime.timedelta(weeks=1)
        users_in_this_week = User.objects.filter(joined_at__gte = to )
        
        users_for_last_weeks = User.objects.filter(joined_at__gte = from_, joined_at__lte = to )
        

        data = {
            'count' : users_in_this_week.count(),
            'percentage' : calc_increase_percentage(currnet_count = users_in_this_week, past_count = users_for_last_weeks) ,

        }
        
        return Response(data,status=status.HTTP_200_OK)

    except Exception as e :
        return Response({'message':f'an error accured : {e}'},status=status.HTTP_400_BAD_REQUEST)