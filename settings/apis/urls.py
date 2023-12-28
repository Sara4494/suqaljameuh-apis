from django.urls import path
from settings.apis.views.page.create import CreatePage
from settings.apis.views.page.update import UpdatePage
from settings.apis.views.page.get import get_pages, get_page
from settings.apis.views.settings.update import UpdateSettings
from settings.apis.views.settings.get import get_settings

urlpatterns = [
    path("page/create/",CreatePage),
    path("page/update/<int:pageid>/",UpdatePage),
    path("update/<int:settingid>/",UpdateSettings),
    path("get/setting/", get_settings),
    path("get/<int:page_id>/", get_page),
    path("get/all/", get_pages),
]