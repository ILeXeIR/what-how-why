from django import forms
from .models import *
from django.contrib.auth.models import User
#from django.core.exceptions import ValidationError
#import re


class AskForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'text', 'tags']
		labels = {'title': 'Title', 'text': 'Question', 'tags': 'Tags'}
		
"""
class AskForm(forms.Form):
	title = forms.CharField(max_length=255, label="Title")
	text = forms.CharField(widget=forms.Textarea, label="Question")
	tags = forms.CharField(max_length=255, label="Tags", required=False)

	def clean_tags(self):
		tags_string = self.cleaned_data['tags']
		tags_string = tags_string.strip().lower()
		if re.match(r'^[\w\s]*$', tags_string):
			tags=set()
			tags_set = set(tags_string.split())
			for tag in tags_set:
				if not Tag.objects.filter(title=tag).first():
					Tag.objects.create(title=tag)
				tags.add(Tag.objects.get(title=tag))
			return tags
		else:
			raise ValidationError('Use only letters, digits or undercover')
"""

class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ['text']
		labels = {'text': ''}

		widgets = {
			'text': forms.Textarea(attrs={
				'class' : 'form-control', 
				'placeholder' : 'Give your answer here.',
				})
		}
