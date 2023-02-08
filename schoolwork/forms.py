from django.forms import ModelForm
from .models import *


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

# class LoginForm(Form):
#     username = CharField(max_length=200)
#     password = CharField(max_length=200,widget=PasswordInput())