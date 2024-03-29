from django.urls import path, include


urlpatterns = [
    path('material/', include('varieties.apis.views.material.urls')),
    path('subcategory/', include('varieties.apis.views.sub_category.urls')),
    path('size/', include('varieties.apis.views.size.urls')),
    path('topstyle/', include('varieties.apis.views.top_style.urls')),
    path('type/', include('varieties.apis.views.type.urls')),
    path('city/', include('varieties.apis.views.city.urls')),
    path('qualification/', include('varieties.apis.views.qualification.urls')),
    path('education/', include('varieties.apis.views.education.urls')),
    path('experience/', include('varieties.apis.views.experience.urls')),
    path('country/', include('varieties.apis.views.country.urls')),
    path('currency/', include('varieties.apis.views.currency.urls')),
    path('amenity/', include('varieties.apis.views.amenity.urls')),
    path('paymentmethod/', include('varieties.apis.views.paymentmethod.urls')),
    path("category/", include("varieties.apis.views.category.urls")),
    path("mechanism/", include("varieties.apis.views.mechanism.urls")),
    path("brand/", include("varieties.apis.views.brand.urls")),
    path("condition/", include("varieties.apis.views.condition.urls")),
    path("color/", include("varieties.apis.views.color.urls")),
    path("rentperiod/", include("varieties.apis.views.rentperiod.urls")),
    path("capacity/", include("varieties.apis.views.capacity.urls")),
    path("kilometer/", include("varieties.apis.views.kilometer.urls")), 
     
    path("os/", include("varieties.apis.views.os.urls")), 
    path("memory/", include("varieties.apis.views.memory.urls")),  
    path("model/", include("varieties.apis.views.model.urls")), 
    path("storage/", include("varieties.apis.views.storage.urls")), 
    path("site/", include("varieties.apis.views.site.urls")), 
    path("subtype/", include("varieties.apis.views.subtype.urls")), 
    path("nearlocation/", include("varieties.apis.views.nearlocation.urls")), 
    path("interface/", include("varieties.apis.views.interface.urls")), 
    path("roomcounts/", include("varieties.apis.views.roomcounts.urls")), 
    path("bathroomcounts/", include("varieties.apis.views.bathroomcounts.urls")),  
    path("floorscounts/", include("varieties.apis.views.floorscounts.urls")),    
    path("buildinage/", include("varieties.apis.views.buildinage.urls")),    
    path("additionalfeature/", include("varieties.apis.views.additionalfeature.urls")),    
    path("adjustedto/", include("varieties.apis.views.adjustedto.urls")),    
    path("estatecountry/", include("varieties.apis.views.estatecountry.urls")),    
    path("estatetype/", include("varieties.apis.views.estatetype.urls")),
    path("transmission-type/", include("varieties.apis.views.transmission_type.urls")),    
    path("regional-specs/", include("varieties.apis.views.regional_specs.urls")),    
    path("internal-specs/", include("varieties.apis.views.internal_specs.urls")),    
    path("foul-type/", include("varieties.apis.views.foul_type.urls")),    
    path("body-type/", include("varieties.apis.views.body_type.urls")),    
    path("outer_specs/", include("varieties.apis.views.outer_specs.urls")),    
] 
       