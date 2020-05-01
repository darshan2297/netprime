from django.forms import ModelForm 
from django import forms
from .models import member


class memberform(forms.ModelForm):
    mid = models.AutoField()
    uname = models.CharField()
    email = models.EmailField()
    first_name = models.CharField()
    last_name = models.CharField()
    password = models.CharField()
    repeat_password = models.CharField()
    mobile_no = models.IntegerField()
    country = models.CharField()
    class Meta:
        model = member
        field = '__all__'
        