from django.urls import path
from teacherapp.views import teacherindex,viewstudents,Viewworks
urlpatterns = [
    path('teacherindex',teacherindex.as_view(),name='teacherindex'),
    path('viewstudents',viewstudents.as_view(),name='viewstudents'),
    path('Viewworks',Viewworks.as_view(),name='Viewworks')

  
]