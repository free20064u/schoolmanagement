
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class StudentForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['image','first_name', 'last_name', 'username', 'email', 'program', 'is_student', 'paid']
        