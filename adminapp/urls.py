from django.urls import path
from adminapp.views import adminindex,verifyparent,ApproveParent,RemoveParent,ListsofParent,KidsProfileDetails,AddTeacher,addprogrammes,viewprogrammes,editprog,Removeprog,ViewComplaints,ViewFeedbacks,ListsofFaculty,Viewadmissions,Accept,Rejectadmission,admissionacceptedlist,assignfaculty
urlpatterns = [
    path('adminindex',adminindex.as_view(),name='adminindex'),
    path('verifyparent',verifyparent.as_view(),name='verifyparent'),
    path('ApproveParent',ApproveParent.as_view(),name='ApproveParent'),
    path('RemoveParent',RemoveParent.as_view(),name='RemoveParent'),
    path('ListsofParent',ListsofParent.as_view(),name='ListsofParent'),
    path('KidsProfileDetails',KidsProfileDetails.as_view(),name='KidsProfileDetails'),
    path('AddTeacher',AddTeacher.as_view(),name='AddTeacher'),
    path('addprogrammes',addprogrammes.as_view(),name='addprogrammes'),
    path('viewprogrammes',viewprogrammes.as_view(),name='viewprogrammes'),
    path('editprog',editprog.as_view(),name='editprog'),
    path('Removeprog',Removeprog.as_view(),name='Removeprog'),
    path('ViewComplaints',ViewComplaints.as_view(),name='ViewComplaints'),
    path('ViewFeedbacks',ViewFeedbacks.as_view(),name='ViewFeedbacks'),
    path('ListsofFaculty',ListsofFaculty.as_view(),name='ListsofFaculty'),
    path('Viewadmissions',Viewadmissions.as_view(),name='Viewadmissions'),
    path('Acceptadmission',Accept.as_view(),name='Acceptadmission'),
    path('Rejectadmission',Rejectadmission.as_view(),name='Rejectadmission'),
    path('admissionacceptedlist',admissionacceptedlist.as_view(),name='admissionacceptedlist'),
    path('assignfaculty',assignfaculty.as_view(),name='assignfaculty'),




]