from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from preschoolapp.models import User, ParentRegistration ,ChildDetails, Faculties , UserType, Programmes, Complaint, Feedback,AdmissionData
from django.core.files.storage import FileSystemStorage

# Create your views here.
class adminindex(TemplateView):
    template_name='admin/index.html'
class verifyparent(TemplateView):
    template_name='admin/approveparent.html'
    def get_context_data(self, **kwargs):
        context = super(verifyparent,self).get_context_data(**kwargs)
        approveparent = ParentRegistration.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')
        context['approveparent'] = approveparent
        return context
class ApproveParent(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name = '1'
        user.save()
        return redirect(request.META['HTTP_REFERER'],{'message':"Account Approved"})
class RemoveParent(View):
    def dispatch(self,request,*args,**kwargs):
        id=request.GET['id']
        pg=User.objects.get(id=id).delete()
       
        return redirect(request.META['HTTP_REFERER'],{'message':"Removed Successfully"})

class ListsofParent(TemplateView):
    template_name='admin/viewparent.html'
    def get_context_data(self, **kwargs):
        view_parent = ParentRegistration.objects.all()
        context = {
            'view_parent':view_parent
        }
        return context

class ListsofFaculty(TemplateView):
    template_name='admin/viewteachers.html'
    def get_context_data(self, **kwargs):
        view_fac = Faculties.objects.all()
        context = {
            'view_fac':view_fac
        }
        return context

class KidsProfileDetails(TemplateView):
    template_name='admin/kidsdetails.html'
    def get_context_data(self, **kwargs):
        id=self.request.GET['id']
        view_parent = ChildDetails.objects.filter(parent_id=id)
        context = {
            'kidpro':view_parent
        }
        return context

class AddTeacher(TemplateView):
    template_name='admin/addteachers.html'
    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        experience = request.POST['experience']
        email = request.POST['email']
        phone = request.POST['phone']
        qualification = request.POST['qualification']
        password = request.POST['password']

        if User.objects.filter(email=email):
            print('pass')
            return render(request, 'admin/addteachers.html' , {'message': "already added the username or email"})
            
        else:
            
            user = User.objects.create_user(username=email, password=password, first_name=name, email=email,
                                            is_staff='0', last_name='1')
            user.save()

            reg = Faculties()# call the model
            reg.user = user
            reg.name=name
            reg.experience=experience
            reg.email=email
            reg.phone = phone
            reg.qualification=qualification
            reg.password = password
            
            reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "teacher"
            usertype.save()
            # messages="Registered Successfully"
            return redirect('adminindex')

class addprogrammes(TemplateView):
    template_name='admin/addprogrammes.html'
    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        agegroup = request.POST['agegroup']
        duration = request.POST['duration']
        fees = request.POST['fees']
        description = request.POST['desc']
        image = request.FILES['image']

        ob=FileSystemStorage()
        obj=ob.save(image.name,image)

        reg = Programmes()# call the model
        reg.name = name
        reg.fees=fees
        reg.duration=duration
        reg.agegroup=agegroup
        reg.description = description
        reg.image=obj
        reg.save()
        return redirect('adminindex')

class viewprogrammes(TemplateView):
    template_name='admin/viewprog.html'
    def get_context_data(self, **kwargs):
        prog = Programmes.objects.all()
        context = {
            'view_programmes':prog
        }
        return context
class editprog(TemplateView):
    template_name='admin/editprog.html'
    def get_context_data(self, **kwargs):
        context = super(editprog, self).get_context_data(**kwargs)
        id3 = self.request.GET['id']
        pro = Programmes.objects.get(id=id3)
        context['upd'] = pro
        return context
    def post(self, request, *args, **kwargs):
        id3 = self.request.GET['id']
        name = request.POST['name']
        agegroup = request.POST['agegroup']
        duration = request.POST['duration']
        fees = request.POST['fees']
        description = request.POST['desc']
        image = request.FILES['image']

        ob=FileSystemStorage()
        obj=ob.save(image.name,image)

        reg = Programmes.objects.get(id=id3)# call the model
        reg.name = name
        reg.fees=fees
        reg.duration=duration
        reg.agegroup=agegroup
        reg.description = description
        reg.image=obj
        reg.save()
        return redirect('adminindex')

class Removeprog(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        Programmes.objects.get(id=id).delete()
        return redirect('adminindex')

class ViewComplaints(TemplateView):
    template_name='admin/viewcomplaints.html'
    def get_context_data(self, **kwargs):
        prog = Complaint.objects.filter(status='Null')
        context = {
            'view_complaint':prog
        }
        return context
    def post(self, request, *args, **kwargs):
        reply=request.POST['reply']
        id = request.POST['id2']
        ob = Complaint.objects.get(id=id)
        ob.reply=reply
        ob.status = 'Complaint Replied'
        ob.save()
        return redirect('ViewComplaints')


class ViewFeedbacks(TemplateView):
    template_name='admin/viewfeedbacks.html'
    def get_context_data(self, **kwargs):
        prog = Feedback.objects.all()
        context = {
            'view_feedback':prog
        }
        return context

class Viewadmissions(TemplateView):
    template_name='admin/viewadmissions.html'
    def get_context_data(self, **kwargs):
        prog = AdmissionData.objects.filter(status='Admission Pending')
        context = {
            'prog':prog
        }
        return context
class Accept(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        adm = AdmissionData.objects.get(pk=id)
        adm.status = 'Admission Accepted'
        adm.save()
        return redirect('Viewadmissions')
class Rejectadmission(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        adm = AdmissionData.objects.get(pk=id)
        adm.status = 'Admission Rejected'
        adm.save()
        return redirect('Viewadmissions')

class admissionacceptedlist(TemplateView):
    template_name='admin/admissionacceptedlist.html'
    def get_context_data(self, **kwargs):
        prog = AdmissionData.objects.filter(status='Admission Accepted')
        view_fac = Faculties.objects.all()

        context = {
            'admsn':prog,'view_fac':view_fac
        }
        return context 
    def post(self, request, *args, **kwargs):

        fac=request.POST['fac']
        id=request.POST['id2']

        adm=AdmissionData.objects.get(id=id)
        adm.faculty_id=fac
        adm.status="Faculty Assigned"
        adm.save()
        return redirect('admissionacceptedlist')


class assignfaculty(TemplateView):
    template_name='admin/assignfaculty.html'
#     def get_context_data(self, **kwargs):
#         context = {
#             'view_fac':view_fac
#         }
#         return context
        
