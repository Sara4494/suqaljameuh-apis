from django.urls import path
from user_profile.apis.views.create import CreateProfile
from user_profile.apis.views.check_username import check_user
from user_profile.apis.views.update import ProfileUpdate
from user_profile.apis.views.get import ProfileInfo, user_details, get_similar_users


urlpatterns = [
    path('me/',ProfileInfo),
    path('user/<int:user_id>/', user_details),
    path('similar-users/<int:user_id>/', get_similar_users),
    path('auth/create/',CreateProfile),
    path('auth/check-username/',check_user),
    path('auth/update-profile/',ProfileUpdate),
]
