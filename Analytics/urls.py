from django.urls import path
from .apis.views.users.users import GetWeklyUsers
from .apis.views.membership.weekly import GetWeklyMembershipsUsers
from .apis.views.ads import featured_published_ads, published_ad

urlpatterns = [
    path('users/weekly/',GetWeklyUsers),
    path('ad/weekly/',published_ad.GetWeklyPublishedAd),
    path('ad/featured/weekly/',featured_published_ads.GetWeklyFuturedPublishedAd),
    path('membership/weekly/',GetWeklyMembershipsUsers),
]