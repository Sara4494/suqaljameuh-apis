from django.urls import path
from varieties.apis.views.condition.create import *
from varieties.apis.views.condition.update import *
from varieties.apis.views.condition.delete import *
from varieties.apis.views.condition.get import *

urlpatterns = [
    path('conditions/',  GetCondition.as_view(), name='get_condition'),
    path('conditions/<int:subcategory>/',  get_conditions, name='get_condition'),
    path('conditions/create/',  CreateCondition.as_view(), name='create_condition'),
    path('conditions/<int:pk>/',  UpdateCondition.as_view(), name='update_condition'),
    path('conditions/<int:pk>/delete/',  DeleteCondition.as_view(), name='delete_condition'),
]