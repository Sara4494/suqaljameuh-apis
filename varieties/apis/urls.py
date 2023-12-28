from django.urls import path ,include

urlpatterns = [
     path ('material/',include('varieties.apis.views.material.urls')),
     path ('sub_category/',include('varieties.apis.views.sub_category.urls')),
     path ('size/',include('varieties.apis.views.size.urls')),
     path ('top_style/',include('varieties.apis.views.top_style.urls')),
     path ('type/',include('varieties.apis.views.type.urls')),
     path ('city/',include('varieties.apis.views.city.urls')),
     path ('qualification/',include('varieties.apis.views.qualification.urls')),
     path ('education/',include('varieties.apis.views.education.urls')),
     path ('experience/',include('varieties.apis.views.experience.urls')),
     path ('country/',include('varieties.apis.views.country.urls')),
     path ('currency/',include('varieties.apis.views.currency.urls')),
     path ('amenity/',include('varieties.apis.views.amenity.urls')),
     path ('paymentmethod/',include('varieties.apis.views.paymentmethod.urls')),
   
    
]