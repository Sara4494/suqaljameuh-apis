from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from varieties.views import Retrievefilters
from varieties.apis.views.brand.create import CreateBrand
from varieties.apis.views.brand.update import UpdateBrand

urlpatterns = [

    path('admin/', admin.site.urls),
    path('user/' , include('users.apis.urls')),
    path('newsletter/',include('newsletter.apis.urls')),
    path('varieties/',include('varieties.apis.urls')),
     path('profile/', include('user_profile.apis.urls')),
     
    
    
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
 
