from celery import shared_task
from Ad.models import AD_TYPES


@shared_task
def reward_user(user, ad):
    if ad.ad_type == AD_TYPES[1][1]:
        user.points = user.points + 25
    if ad.ad_type == AD_TYPES[1][1]:
        user.points = user.points + 50
