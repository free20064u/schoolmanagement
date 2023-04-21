from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Program, Student

# Create your views here.
def index (request):
  return render(request, 'course/index.html')


def student(request):
  users = User.objects.all().order_by('username')

  context = {
    'users': users
  }

  return render(request, 'course/student.html', context)
