from Ad.models import AD_TYPES
from users.models import USER_RANKS


def update_ad_type(membership, ad):
    if membership.pk == 2:
        ad.ad_type = AD_TYPES[1][1]
        ad.save()
    if membership.pk == 3:
        ad.ad_type = AD_TYPES[0][0]
        ad.save()


def update_user_rank(membership, user):
    if membership.pk == 2:
        user.user_rank = USER_RANKS[1][1]
        user.save()
    if membership.pk == 3:
        user.user_rank = USER_RANKS[0][0]
        user.save()
