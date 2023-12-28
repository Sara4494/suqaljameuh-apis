
from .task import SendNotification



def Bridge ( user_id ) : 
    SendNotification.delay(user_id=user_id)
    return True