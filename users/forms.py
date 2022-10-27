from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['avatar']

	def clean_avatar(self):
		avatar = self.cleaned_data.get('avatar', False)
		if avatar and avatar.size > 1024*1024:
			raise ValidationError("Image size can't exceed 1 MB")
		return avatar
