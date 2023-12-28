from django.urls import path
from varieties.apis.views.brand.create import CreateBrand
from varieties.apis.views.brand.update import UpdateBrand
from varieties.apis.views.brand.delete import DeleteBrand
from varieties.apis.views.brand.get import GetBrand, get_brands

urlpatterns = [
    path("create/", CreateBrand.as_view()),
    path('brands/<int:pk>/update/', UpdateBrand.as_view()),
    path('brands/<int:pk>/delete/', DeleteBrand.as_view()),
    path('brands/', GetBrand.as_view()),
    path('brands/<int:subcategory_id>/', get_brands),
]
