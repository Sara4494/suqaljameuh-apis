from Ad.models import Ad
from rest_framework.response import Response
from rest_framework import decorators, status, permissions
import datetime
from ..calc_increase import calc_increase_percentage


@decorators.api_view(["GET"])
@decorators.permission_classes([permissions.IsAdminUser])
def GetWeklyPublishedAd (request) : 
    try : 
        
        to = datetime.datetime.now() - datetime.timedelta(weeks=1)
        from_ = to - datetime.timedelta(weeks=1)
        ads_in_this_week = Ad.objects.filter(published_at__gte = to )
        
        ads_for_last_weeks = Ad.objects.filter(published_at__gte = from_, published_at__lte = to )
        



        data = {
            'count' : ads_in_this_week.count(),
            'percentage' : calc_increase_percentage(currnet_count = ads_in_this_week, past_count =ads_for_last_weeks) ,
        }

        return Response(data,status=status.HTTP_200_OK)

    except Exception as e :
        return Response({'message':f'an error accured : {e}'},status=status.HTTP_400_BAD_REQUEST)