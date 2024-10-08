from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from parentapp.forms import ChildForm
from preschoolapp.models import UserType,ParentRegistration,ChildDetails,Programmes,Feedback,Faculties,Complaint,AdmissionData,Activity
from django.contrib import messages
from datetime import date

# Create your views here.
class parentindex(TemplateView):
    template_name='parent/index.html'

def add_child(request):
    form = ChildForm()
    xyz=ParentRegistration.objects.get(user_id=request.user.id)

    if request.method == 'POST':
        form = ChildForm(request.POST, request.FILES)
        
        if form.is_valid():
            de = form.save(commit=False)
            de.parent_id=xyz.id
            de.save()
            messages.success(request, 'Child Details Added Successfully')

            return redirect('addkiddetails')
    return render(request, 'parent/addkid.html', {'form': form})

class KidsProfile(TemplateView):
    template_name = 'parent/kidspro.html'
    def get_context_data(self, **kwargs):
        id1 = self.request.user.id
        parent = ParentRegistration.objects.get(user_id=id1)
        kidpro = ChildDetails.objects.filter(parent_id=parent.id)
       
        context = {
            'kidpro':kidpro
        }
        return context


def edit_kids(request,id):
    xy=ParentRegistration.objects.get(user_id=request.user.id)

    kids=ChildDetails.objects.get(id=id)
    form=ChildForm(instance=kids)

    if request.method == 'POST':
        form = ChildForm(request.POST,request.FILES,instance=kids)
        
        if form.is_valid():
           
            de = form.save(commit=False)
            de.parent_id=xy.id
            de.save()
            messages.success(request, 'Child Details updated Successfully')

            return redirect('edit_kids',id=id)
    return render(request, 'parent/kidsproedit.html', {'form': form,'kids':kids})

class AddProgrammes(TemplateView):
    template_name='parent/program.html'
    def get_context_data(self, **kwargs):
        prog = Programmes.objects.all()
        context = {
            'programme':prog
        }
        return context

class AddFeedback(TemplateView):
    template_name = 'parent/feedback.html'
    def post(self, request, *args, **kwargs):
        xy=ParentRegistration.objects.get(user_id=request.user.id)
        subject = request.POST['subject']
        messages = request.POST['fb']
        rate = request.POST['rate']
        reg = Feedback()# call the model
        reg.parent_id = xy.id
        reg.rate=rate
        reg.subject=subject
        reg.messages=messages
        reg.save()
        return redirect('parentindex')

class AddComplaint(TemplateView):
    template_name = 'parent/complaint.html'
    def get_context_data(self, **kwargs):
        fac = Faculties.objects.all()
        xy=ParentRegistration.objects.get(user_id=self.request.user.id)
        kid = ChildDetails.objects.filter(parent_id=xy.id)
        context= {'fac':fac,'parent':xy,'kid':kid}
        return context
    def post(self, request, *args, **kwargs):
        xy=ParentRegistration.objects.get(user_id=request.user.id)
        complaint=request.POST['complaint']
        kid=request.POST['kid']
        fac=request.POST['faculty']
        com=Complaint()
        com.parent_id=xy.id
        
        com.child_id=kid
        com.fac_id=fac
        com.complaintmessages=complaint
        com.save()
        return redirect('parentindex')

class ViewReply(TemplateView):
    template_name='parent/viewcomplaintreply.html'
    def get_context_data(self, **kwargs):
        xy=ParentRegistration.objects.get(user_id=self.request.user.id)

        prog = Complaint.objects.filter(parent_id=xy.id)
        context = {
            'view_complaint':prog
        }
        return context

class Admission(TemplateView):
    template_name='parent/admission.html'
    def get_context_data(self, **kwargs):
        id1 = self.request.user.id
        parent = ParentRegistration.objects.get(user_id=id1)
        kidpro = ChildDetails.objects.filter(parent_id=parent.id)
       
        context = {
            'kidpro':kidpro,'parent':parent
        }
        return context
    def post(self, request, *args, **kwargs):
        xy=ParentRegistration.objects.get(user_id=request.user.id)
        id=self.request.GET['id']
        kid=request.POST['kid']


        adm=AdmissionData()
        adm.parent_id=xy.id
        adm.child_id=kid
        adm.programme_id=id
        adm.status ='Admission Pending'
        adm.save()
        return redirect('parentindex')

class viewadmission(TemplateView):
    template_name='parent/kidsadmission.html'
    def get_context_data(self, **kwargs):
        id1 = self.request.user.id
        parent = ParentRegistration.objects.get(user_id=id1)
        kidpro = AdmissionData.objects.filter(parent_id=parent.id)
        context = {
            'kidpro':kidpro,
        }
        return context

class Viewlessons(TemplateView):
    template_name='parent/viewlessons.html'
    def get_context_data(self, **kwargs):
        
        xy=ParentRegistration.objects.get(user_id=self.request.user.id)

        prog = Activity.objects.filter(admission__parent_id=xy.id)
        context = {
            'view_lesson':prog
        }
        return context

class ViewActivities(TemplateView):
    template_name='parent/viewactivity.html'
    def get_context_data(self, **kwargs):
        
        xy=ParentRegistration.objects.get(user_id=self.request.user.id)

        prog = Activity.objects.filter(admission__parent_id=xy.id,status='Works Upload')
        context = {
            'view_lesson':prog
        }
        return context
    def post(self, request, *args, **kwargs):
        xy=ParentRegistration.objects.get(user_id=request.user.id)
        id=self.request.POST['id2']
        current_date = date.today()
        uploadwork=request.FILES['uploadwork']
        activity=Activity.objects.get(id=id)
        activity.uploadwork=uploadwork
        
        activity.status='Work Completed'
        activity.save()
        return redirect('parentindex')

        







    



       






























# class addkiddetails(TemplateView):
#     template_name = 'parent/addkid.html'
#     def post(self, request, *args, **kwargs):
#         xyz=ParentRegistration.objects.get(user_id=self.request.user.id)
#         name = request.POST['name']
#         age = request.POST['age']
#         birth = request.FILES['birth']
#         image = request.FILES['image']
#         fi = FileSystemStorage()
#         birth = fi.save(birth.name, birth)
#         image = fi.save(image.name, image)
#         reg = ChildDetails()# call the model
#         reg.parent_id = xyz.id
#         reg.name=name
#         reg.age=age
#         reg.birthcertificate=birth
#         reg.image = image
#         reg.save() 
#         # messages.success(request, "Child Details Added Successfully")
#         return redirect ('parentindex')
#         # return redirect('parent:index',{'message':"Child Details Added Successfully"})



       