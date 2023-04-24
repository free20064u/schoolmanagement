
from django import forms
from .models import CustomUser, Program
from django.contrib.auth.forms import UserCreationForm


class StudentForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['image','first_name', 'last_name', 'username','indexNo', 'email', 'program', 'paid']
        

class ProgramForm(forms.ModelForm): 
    class Meta:
        model = Program
        fields = '__all__'


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email','first_name', 'last_name','is_student')
        widgets = {
            'is_student':forms.HiddenInput(attrs={'value':'0'})
        }