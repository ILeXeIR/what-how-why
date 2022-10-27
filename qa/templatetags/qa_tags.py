from django import template
from qa.models import *

register = template.Library()

"""
@register.simple_tag()
def get_popular_tags():
	return Question.tags.most_common()[:5]
"""

@register.inclusion_tag('popular_tags.html')
def show_popular_tags():
	p_tags = Question.tags.most_common()[:10]
	return {'popular_tags': p_tags}