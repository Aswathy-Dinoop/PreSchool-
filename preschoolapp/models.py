from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserType(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type=models.CharField(max_length=10,null=True)
class ParentRegistration(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    fname=models.CharField(max_length=50,null=True)
    lname=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=50,null=True)
    location=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)
class ChildDetails(models.Model):
    parent=models.ForeignKey(ParentRegistration,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50,null=True,blank=False)
    age=models.IntegerField()
    birthcertificate=models.FileField(null=True,blank=False)
    image=models.ImageField(null=True)
    MALE = 'Male'
    FEMALE = 'Female'
    
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    gender=models.CharField(max_length=10,default='Male',choices=GENDER_CHOICES,null=True)

class Faculties(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50,null=True,blank=False)
    email=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=50,null=True)
    qualification=models.CharField(max_length=50,null=True)
    experience=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)

class Programmes(models.Model):
    name=models.CharField(max_length=50,null=True,blank=False,unique=True)
    duration=models.CharField(max_length=50,null=True,blank=False)
    fees=models.CharField(max_length=50,null=True,blank=False)
    image=models.ImageField(null=True,unique=True)
    description=models.CharField(max_length=50,null=True,blank=False)
    agegroup=models.CharField(max_length=50,null=True,blank=False,unique=True)

class Feedback(models.Model):
    parent=models.ForeignKey(ParentRegistration,on_delete=models.CASCADE,null=True)
    subject=models.CharField(max_length=50,null=True,blank=False)
    rate=models.CharField(max_length=50,null=True,blank=False)
    messages=models.CharField(max_length=50,null=True,blank=False)

class Complaint(models.Model):
    parent=models.ForeignKey(ParentRegistration,on_delete=models.CASCADE,null=True)
    child=models.ForeignKey(ChildDetails,on_delete=models.CASCADE,null=True)
    fac=models.ForeignKey(Faculties,on_delete=models.CASCADE,null=True)
    complaintmessages=models.CharField(max_length=50,null=True,blank=False)
    reply=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=100,null=True)

class AdmissionData(models.Model):
    parent=models.ForeignKey(ParentRegistration,on_delete=models.CASCADE,null=True)
    child=models.ForeignKey(ChildDetails,on_delete=models.CASCADE,null=True)
    programme=models.ForeignKey(Programmes,on_delete=models.CASCADE,null=True)
    faculty=models.ForeignKey(Faculties,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=100,null=True)

class Activity(models.Model):
    admission=models.ForeignKey(AdmissionData,on_delete=models.CASCADE,null=True)
    faculty=models.ForeignKey(Faculties,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=100,null=True)
    lessons=models.ImageField(null=True)
    video=models.ImageField(null=True)
    uploaddate=models.DateTimeField(auto_now_add=True,null=True)
    submissiondate=models.CharField(max_length=100,null=True)
    uploadwork=models.ImageField(max_length=100,null=True)
