from django.urls import path
from varieties.apis.views.category.create import create_category
from varieties.apis.views.category.update import update_category
from varieties.apis.views.category.delete import delete_category
from varieties.apis.views.category.get import GetCategory

urlpatterns = [
    path("create/", create_category),
    path("update/<int:category_id>/", update_category),
    path("delete/<int:category_id>/", delete_category),
    path("get/", GetCategory.as_view()),
]
