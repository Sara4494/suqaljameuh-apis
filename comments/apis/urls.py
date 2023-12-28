from django.urls import path
from comments.apis.views.create import add_comment
from comments.apis.views.delete import delete_comment
from comments.apis.views.get import get_user_comments, get_ad_comments

urlpatterns = [
    path("add-comment/<int:ad_id>/", add_comment),
    path("delete-comment/<int:comment_id>/", delete_comment),
    path("user-comments/", get_user_comments),
    path("ad-comments/<int:ad_id>/", get_ad_comments),
]
