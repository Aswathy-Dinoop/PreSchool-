from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login, authenticate
from preschoolapp.models import UserType,ParentRegistration

# Create your views here.
class index(TemplateView):
    template_name = 'index.html'
class about(TemplateView):
    template_name = 'about.html'
class contact(TemplateView):
    template_name = 'contact.html'
class register(TemplateView):
    template_name = 'register.html'
    def post(self, request, *args, **kwargs):
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        location = request.POST['location']
        password = request.POST['password']

        if User.objects.filter(email=email):
            print('pass')
            return render(request, 'register.html' , {'message': "already added the username or email"})
            
        else:
            
            user = User.objects.create_user(username=email, password=password, first_name=fname, email=email,
                                            is_staff='0', last_name='0')
            user.save()

            reg = ParentRegistration()# call the model
            reg.user = user
            reg.fname=fname
            reg.lname=lname
            reg.email=email
            reg.phone = phone
            reg.location=location
            reg.password = password
            
            reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "parent"
            usertype.save()
            # messages="Registered Successfully"
            return redirect('/',{'message':"Registered Successfully"})


class loginn(TemplateView):
    template_name = 'login.html'
    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email,password=password)

        if user is not None:
            login(request,user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('adminindex')
                elif UserType.objects.get(user_id=user.id).type == "parent":
                    return redirect('parentindex')
                elif UserType.objects.get(user_id=user.id).type == "teacher":
                    return redirect('teacherindex')
                
            else:
                # messages.add_message(request, messages.INFO, "Hello world.")
                return render(request, 'login.html', {'message': " User Account Not Authenticated"})
        else:
            return render(request, 'login.html', {'message': "Invalid Username or Password"})