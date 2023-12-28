from rest_framework.response import Response
from rest_framework import decorators, status, permissions
import datetime
from ..calc_increase import calc_increase_percentage
from memberships.models import UserMembership


@decorators.api_view(["GET"])
@decorators.permission_classes([permissions.IsAdminUser])
def GetMonthlyMembershipsUsers (request) : 
    try : 
        
        to = datetime.datetime.now() - datetime.timedelta(weeks=4)
        from_ = to - datetime.timedelta(weeks=4)
        users_in_this_week = UserMembership.objects.filter(subscribed_at__gte = to )
        
        users_for_last_weeks = UserMembership.objects.filter(subscribed_at__gte = from_, subscribed_at__te = to )
        

        data = {
            'count' : users_in_this_week.count(),
            'percentage' : calc_increase_percentage(currnet_count = users_in_this_week, past_count = users_for_last_weeks) ,
        }
        
        return Response(data,status=status.HTTP_200_OK)

    except Exception as e :
        return Response({'message':f'an error accured : {e}'},status=status.HTTP_400_BAD_REQUEST)