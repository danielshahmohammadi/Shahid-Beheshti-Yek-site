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

from apps import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gallerylist/', views.gallerylist, name='gallerylist'),
    path('contanct_use/', views.contanct_use, name='contanct_use'),
    path('newslist/', views.newslist, name='newslist'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('studentview/', views.studentview, name='studentview'),
    path('lessons/', views.lessons, name='lessons'),
    path('gheybat_list/', views.gheybat_list, name='gheybat_list'),
    path('gradelist/', views.gradelist, name='gradelist'),
    path('wekkly_program/', views.wekkly_program, name='wekkly_program'),
    path('st_darslist/', views.st_darslist, name='st_darslist'),
    path('changepwd/', views.changepwd, name='changepwd'),
    path('honnors/', views.honnors, name='honnors'),
    path('school_staff/', views.school_staff, name='school_staff'),
    path('weblog/', views.weblog, name='weblog'),
    path('pishnahadatlis/', views.pishnahadatlis, name='pishnahadatlis'),
    path('facilitys/', views.facilitys, name='facilitys'),
]
