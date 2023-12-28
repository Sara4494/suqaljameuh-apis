from django.urls import path
from .views.reportad.create import make_report
from .views.reportad.get import *
from .views.reportad.update import *

from .views.reportproblem.create import *
from .views.reportproblem.get import *
from .views.reportproblem.update import *
from .views.favorites.create import *
from .views.favorites.get import *
from .views.favorites.delete import *

from .views.reportcomment.get import Get_Comments_Reports, comment_report
from .views.reportcomment.create import Create_Comment_Report
from .views.reportcomment.delete import Delete_Comments_Reports
from .views.reportcomment.update import Update_Comments_Reports

urlpatterns = [
    path('make-report/', make_report),
    path('all/', retrieve_reports),
    path('report/<int:report_id>/', retrieve_single_report),
    path('reports/discard/<int:report_id>/',
         discard_report, name='discard_report'),
    path('reports/update/in-progress/<int:report_id>/',
         flag_report_in_progress, name='flag_report_in_progress'),
    path('reports/update/finalized/<int:report_id>/',
         flag_report_finalized, name='flag_report_finalized'),
    path('make-problem-reports/',  make_problems),
    path('problems/',  retrieve_problems),
    path('problems/<int:problem_id>/',  retrieve_single_problem),
    path('problems/<int:problem_id>/discard/',  discard_problem),
    path('problems/<int:problem_id>/in-progress/',  flag_problem_in_progress),
    path('problems/finalized/<int:problem_id>/',
         flag_problem_finalized, name='flag_problem_finalized'),
    path('favorites/', retrieve_favorites),
    path('favorites/add/<int:ad_id>/',  add_to_favorite),
    path('favorites/delete/<int:favorite_id>/',  delete_favorite),

     # comments report
     path('comments/get/',Get_Comments_Reports), # is admin permissions [GET]
     path('comments/get/<int:report_id>/', comment_report), # is admin permissions [GET]
     path('comments/create/<int:comment_id>/',Create_Comment_Report),       # is authenticated permissions [POST]
     path('comments/delete/<int:report_id>/',Delete_Comments_Reports), # //     //          //  [DELETE]
     path('comments/update/<int:report_id>/',Update_Comments_Reports), # //    //          //   [PUT]

]
