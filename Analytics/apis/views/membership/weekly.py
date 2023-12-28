from rest_framework.response import Response
from rest_framework import decorators, status, permissions
import datetime
from ..calc_increase import calc_increase_percentage
from django.utils.timezone import get_current_timezone
from memberships.models import UserMembership


@decorators.api_view(["GET"])
@decorators.permission_classes([permissions.IsAdminUser])
def GetWeklyMembershipsUsers (request) : 
    try : 
        
        
        data = []
        for i in range(0,7) :
            date = datetime.datetime.now(tz=get_current_timezone()) - datetime.timedelta(days=i)
            members = UserMembership.objects.filter(subscribed_at=date)

            profit = 0

            for member in members : 
                profit += member.membership.price

            data.append({
                'date' : f'{date.date()}' ,
                'count' : members.count() ,
                'profit' : profit
            })

        return Response(data,status=status.HTTP_200_OK)

    except Exception as e :
        return Response({'message':f'an error accured : {e}'},status=status.HTTP_400_BAD_REQUEST)