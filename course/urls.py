"""
URL configuration for schoolmanagement project.

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
from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/', views.student, name='student' ),
    path('student_details/<int:id>/', views.student_details, name='student_details'),
    path('add_student/', views.add_student, name='add_student'),
    path('delete_student/<int:pk>', views.delete_student, name='delete_student'),
    path('edit_student/<int:pk>',views.edit_student, name='edit_student' ),
    path('search_student', views.search_student, name='search_student'),
    path('program/', views.program, name='program'),
    path('edit_program/<int:id>/', views.edit_program, name='edit_program'),
    path('logout-user', views.logout_user, name='logout_user'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/', views.users, name='users'),
    path('user_details/<int:id>/', views.user_details, name='user_details'),
    ] 
