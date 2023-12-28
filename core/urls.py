from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from varieties.views import Retrievefilters
from rest_framework_simplejwt.views import TokenRefreshView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [

    path('admin/', admin.site.urls),
    path('user/', include('users.apis.urls')),
    path('ads/', include('Ad.apis.urls')),
    path("fashion-ads/", include("menfashion.apis.urls")),
    path("electronics-ads/", include("electronics.apis.urls")),
    path("cars-ads/", include("cars.apis.urls")),
    path("apartments-ads/", include("apartments.apis.urls")),
    path("computers-ads/", include("computers.apis.urls")),
    path("education-ads/", include("education.apis.urls")),
    path("motorbikes-ads/", include("motorbikes.apis.urls")),
    path("filters/", include("filters.apis.urls")),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("comments/", include("comments.apis.urls")),
    path('newsletter/', include('newsletter.apis.urls')),
    path("notification-settings/", include("notification.apis.urls")),
    path('varieties/', include('varieties.apis.urls')),
    path('profile/', include('user_profile.apis.urls')),
    path('chat/', include('chat.urls')),
    path('reports/', include('reports.apis.urls')),
    path('memberships/', include('memberships.apis.urls')),
    path('analytics/',include('Analytics.urls')),
    path('jobs/',include('jobs.apis.urls')),
    path("settings/",include('settings.apis.urls')),

] 
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

