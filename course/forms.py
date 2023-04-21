from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
        model = ''
        fields = '__all__'
        