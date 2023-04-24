from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import StudentForm, ProgramForm, RegisterForm
from .models import Program, CustomUser

# Create your views here.
def index (request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate( request, username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, 'logged in successfully.')
      return redirect('student')
  return render(request, 'course/index.html')

def register(request):
  form = RegisterForm()
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Successfully registered. Login now.')
      return redirect('index')
    else:
      messages.error(request, 'Registration not successfull.')

  context = {
    'form': form,
  }
  return render(request, 'course/register.html', context)


def logout_user(request):
  logout(request)
  messages.success(request, 'logged out successfully.')
  return redirect('index')


@login_required( login_url='index')
def student(request):
  users = CustomUser.objects.filter(Q(is_student=True) & Q(is_superuser=False))
  print(users)
  context = {
    'users': users,
  }
  return render(request, 'course/student.html', context)


@login_required( login_url='index')
def student_details(request, id=None):
  student = get_object_or_404(CustomUser, id=id)
  context = {
    'student': student,
  }
  return render(request, 'course/student_details.html', context)


@login_required( login_url='index')
def add_student(request):

  context = {}
  studentForm = StudentForm()
  if request.method == 'POST':
    studentForm = StudentForm(request.POST , request.FILES)
    if studentForm.is_valid():
      studentForm.save()
      studentForm = StudentForm()
      messages.success(request, 'student successfully registered.')
    else:
      messages.error(request, 'student not registered.')

  context['studentForm'] = studentForm
  return render(request, 'course/add_student.html', context)


@login_required( login_url='index')
def delete_student(request, pk=None):
  student = get_object_or_404(CustomUser, id=pk)
  student.delete()
  messages.success(request, 'Student deleted successfully')
  return redirect('student')


@login_required( login_url='index')
def edit_student(request, pk=None):
  student = CustomUser.objects.get(id=pk)
  studenForm = StudentForm(instance=student)

  if request.method == "POST": 
    studentForm = StudentForm(request.POST,request.FILES,  instance=student)
    if studentForm.is_valid():              
      studentForm.save()
      messages.success(request, 'Student iformation updated.')
      return redirect('student')
    else:
      messages.error(request, 'Student information not updated.')
      
  context = {
    'studentForm': studenForm
  }
  return render (request, 'course/add_student.html', context)


@login_required( login_url='index')
def search_student(request):
  if request.method == "POST":
    name = request.POST['name']
    print(name)
  context = {}
  return redirect('student', context)


@login_required( login_url='index')
def program(request):

  programs = Program.objects.all().order_by('programName')
  programForm = ProgramForm(request.POST or None)
  
  if request.method == "POST":
    program = Program.objects.filter(programName=request.POST['programName'])
    print(program)
    if program :
      if programForm.is_valid():
        programForm.save() 
        programForm = ProgramForm()
        messages.success(request, 'New program added')
      else:
        messages.error(request, 'Program not added')
    else:
      messages.error(request, 'Program already exist')
      
  context = {
    'programs': programs,
    'programForm': programForm
  }
  return render(request, 'course/program.html', context)


@login_required(login_url='index')
def edit_program(request, id=None):
  program = Program.objects.get(id=id)
  programs = Program.objects.all()
  programForm = ProgramForm(instance=program)
  if request.method == "POST":
    programForm = ProgramForm(request.POST, instance=program)
    if programForm.is_valid():
      programForm.save()
      programForm = ProgramForm()
      messages.success(request, 'Program successfully updated')
      return redirect('program')
    else:
      messages.error(request, 'Program not updated')

  context = {
    'programs': programs,
    'programForm': programForm
  }
  
  return render(request, 'course/program.html', context)
@login_required(login_url='index')
def dashboard(request):
  admins = CustomUser.objects.filter(is_superuser=True)
  students = CustomUser.objects.filter(Q(is_student=True) & Q(is_superuser=False))
  users = CustomUser.objects.filter(Q(is_student=False) & Q(is_superuser=False))
  programs = Program.objects.all()

  total_fees = 0
  total_balance = 0
  paid = 0
  for student in students:
    total_fees = total_fees + int(student.program.fees)
    total_balance = total_balance + int(student.bal())
    paid = paid + int(student.paid)



  context = {
    'admins': admins,
    'students': students,
    'users': users,
    'programs': programs,
    'total_fees': total_fees,
    'total_balance': total_balance,
    'paid': paid,
	}
  return render(request, 'course/dashboard.html', context)