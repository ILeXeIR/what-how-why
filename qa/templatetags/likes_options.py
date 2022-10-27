from django import template
from django.contrib.auth.models import User
from qa.models import *

register = template.Library()

def count_likes(obj):
	return obj.likes.all().count()

def check_like(obj, user_id):
	if obj.likes.filter(id=user_id):
		return True
	else:
		return False

@register.inclusion_tag('q_like_button.html')
def q_like_button(question, user_id, url_from):
	likes_count = count_likes(question)
	is_liked = check_like(question, user_id)
	return {'question': question, 'url_from': url_from, 
			'likes_count': likes_count, 'is_liked': is_liked}

@register.inclusion_tag('a_like_button.html')
def a_like_button(answer, user_id, url_from):
	likes_count = count_likes(answer)
	is_liked = check_like(answer, user_id)
	return {'answer': answer, 'url_from': url_from, 
			'likes_count': likes_count, 'is_liked': is_liked}