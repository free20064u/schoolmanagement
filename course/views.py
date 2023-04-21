from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from .forms import StudentForm
from .models import Program, CustomUser

# Create your views here.
def index (request):
  return render(request, 'course/index.html')


def student(request):
  users = CustomUser.objects.all().order_by('first_name')
  print(users)
  context = {
    'users': users,
  }

  return render(request, 'course/student.html', context)


def student_details(request, id=None):
  student = get_object_or_404(CustomUser, id=id)
  context = {
    'student': student,
  }
  return render(request, 'course/student_details.html', context)


def add_student(request):

  context = {}
  studentForm = StudentForm(request.POST or None, request.FILES or None)
  if studentForm.is_valid():
    studentForm.save()


  context['studentForm'] = studentForm
  
  return render(request, 'course/add_student.html', context)