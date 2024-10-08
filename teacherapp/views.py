from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from preschoolapp.models import Faculties,ParentRegistration,AdmissionData,Activity

# Create your views here.
class teacherindex(TemplateView):
    template_name='faculty/index.html'
class viewstudents(TemplateView):
    template_name='faculty/viewstudents.html'
    def get_context_data(self, **kwargs):
        id1 = self.request.user.id
        faculty = Faculties.objects.get(user_id=id1)
        view_fac = AdmissionData.objects.filter(faculty_id=faculty.id)
        context = {
            'view_fac':view_fac
        }
        return context
    def post(self, request, *args, **kwargs):
        xy=Faculties.objects.get(user_id=request.user.id)
        id=self.request.POST['id2']
        lesson=request.FILES['lesson']
        activity=request.FILES['activity']
        subdate=request.POST['subdate']


        work=Activity()
        work.admission_id=id
        work.lessons=lesson
        work.video=activity
        work.faculty_id=xy.id
        work.submissiondate=subdate
        work.status='Works Upload'
        work.save()
        return redirect('teacherindex')


class Viewworks(TemplateView):
    template_name='faculty/viewstudentsworks.html'
    def get_context_data(self, **kwargs):
        
        xy=Faculties.objects.get(user_id=self.request.user.id)

        prog = Activity.objects.filter(faculty_id=xy.id,status='Work Completed')
        context = {
            'view_lesson':prog
        }
        return context
   

