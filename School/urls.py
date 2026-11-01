"""
URL configuration for School project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Classes.views import home,gallerylist,about,login,gheybat_list,pishnahadatlis,dashboard,studentview,wekkly_program,st_darslist,changepwd,gradelist,studentview,contanct_use,school_staff,newslist,lessons,honnors,weblog,facilitys


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('about/',about),
    path('gallerylist/',gallerylist),
    path('contanct_use/',contanct_use),
    path('newslist/',newslist),
    path('login/',login),
    path('dashboard/',dashboard),
    path('studentview/',studentview),
    path('lessons/',lessons),
    path('gheybat_list/',gheybat_list),
    path('gradelist/',gradelist),
    path('wekkly_program/',wekkly_program),
    path('st_darslist/',st_darslist),
    path('changepwd/',changepwd),
    path('honnors/',honnors),
    path('school_staff/',school_staff),
    path('weblog/',weblog),
    path('pishnahadatlis/',pishnahadatlis),
    path('facilitys/',facilitys),

]
