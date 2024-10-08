from django.urls import path
from parentapp.views import parentindex,KidsProfile,AddProgrammes,AddFeedback,AddComplaint,ViewReply,Admission,viewadmission,Viewlessons,ViewActivities
from parentapp import views
urlpatterns = [
    path('parentindex',parentindex.as_view(),name='parentindex'),
    path('addkiddetails',views.add_child,name='addkiddetails'),
    path('kidsprofile',KidsProfile.as_view(),name='kidsprofile'),
    # path('singlekidprofileedit',kidsprofileedit.as_view(),name='singlekidprofileedit'),
    path('edit_kids/<int:id>',views.edit_kids,name='edit_kids'),
    path('Programmes',AddProgrammes.as_view(),name='Programmes'),
    path('AddFeedback',AddFeedback.as_view(),name='AddFeedback'),
    path('AddComplaint',AddComplaint.as_view(),name='AddComplaint'),
    path('ViewReply',ViewReply.as_view(),name='ViewReply'),
    path('Admission',Admission.as_view(),name='Admission'),
    path('viewadmission',viewadmission.as_view(),name='viewadmission'),
    path('Viewlessons',Viewlessons.as_view(),name='Viewlessons'),
    path('ViewActivities',ViewActivities.as_view(),name='ViewActivities')



]