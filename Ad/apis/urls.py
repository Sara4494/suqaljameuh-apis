from django.urls import path
from .views.get import GetAllAds, get_ad, get_category_ads, get_user_ads, get_seller_ads, get_related_ads, get_featured_ads, get__all
from .views.delete import delete_ad, delete_ads
from .views.create import publish_ad, rate_ad
from .views.search import search_ads


urlpatterns = [
    path('get-all/', GetAllAds),
    path('get-featured/', get_featured_ads),
    path('get-category/<str:category_name>/', get_category_ads),
    path('get-related/<int:ad_id>/<int:subcategory_id>/', get_related_ads),
    path('user-ads/', get_user_ads),
    path('seller-ads/<int:user_id>/', get_seller_ads),
    path('publish/', publish_ad),
    path('rate/<int:ad_id>/', rate_ad),
    path('search/', search_ads),
    path('get/<int:ad_id>/', get_ad),
    path('delete/<int:ad_id>/', delete_ad),
    path('delete/', delete_ads),
]
