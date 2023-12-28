from django.urls import path
from .views.create import *
from .views.delete import delete
from .views.get import get_users, get_featured_users, get_featured_membership, get_membership
from .views.update import update, update_user_data
from .auth.user.register import register
from .auth.user.login import login
from .auth.admin.login import admin_login
from .auth.admin.create import create_admin
from .auth.verify import verify_otp
from .views.follow import *

urlpatterns = [
    path('create/', create),
    path('update/', update),
    path('update-info/', update_user_data),
    path('delete/', delete),
    path('get/', get_users),
    path('rate/<int:user_id>/', rate_user),
    path('get-featured/', get_featured_users),
    path('get-membership/', get_membership),
    path('get-featured-membership/', get_featured_membership),

    # authentication for custom user
    path('auth/register/', register),
    path('auth/login/', login),


    # authentication for admin
    path('auth/admin/login/', admin_login),
    path('auth/admin/create/', create_admin),

    path('follow/', follow),
    path('unfollow/', unfollow),

    # OTP Verification
    path('otp/verify/', verify_otp),
]
