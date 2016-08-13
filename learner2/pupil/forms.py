from django import forms
from django.forms import ModelForm,widgets
from pupil.models import User_info,User_data

class User_infoForm(forms.ModelForm) :
	name = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput())
	emailid = forms.CharField(widget=forms.EmailInput())
	personal = forms.Textarea()
	
	class Meta:
		model = User_info
		fields = ['name','password','emailid']

class LoginForm(forms.Form) :
	name = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		ordering = ["name"]
		

