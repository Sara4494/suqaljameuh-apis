from ..calc_increase import calc_increase_percentage
from memberships.models import UserMembership
import datetime



def Make_Member_Anylisis (days) :
    to = datetime.datetime.now() - datetime.timedelta(days=days)
    from_ = to - datetime.timedelta(days=days)
    users_in_this_moment = UserMembership.objects.filter(subscribed_at__gte = to )
    
    users_for_last_moment = UserMembership.objects.filter(subscribed_at__gte = from_, subscribed_at__te = to )
    


    data = {
        'count' : users_in_this_moment.count(),
        'percentage' : calc_increase_percentage(currnet_count = users_in_this_moment, past_count = users_for_last_moment) ,
    }
        
    return data