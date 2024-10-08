"""
URL configuration for preschool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from preschoolapp.views import index,about,contact,register,loginn


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',index.as_view(),name='index'),
    path('about/',about.as_view(),name='about'),
    path('contact/',contact.as_view(),name='contact'),
    path('register/',register.as_view(),name='register'),
    path('login/',loginn.as_view(),name='login'),
    path('',include('adminapp.urls')),
    path('',include('parentapp.urls')),
    path('',include('teacherapp.urls')),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

