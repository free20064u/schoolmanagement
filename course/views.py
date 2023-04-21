from django.shortcuts import get_object_or_404, render
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


def student_details(request, id=None):
  student = get_object_or_404(User, id=id)
  context = {
    'student': student,
  }
  return render(request, 'course/student_details.html', context)