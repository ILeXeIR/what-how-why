#URLs for app 'qa'

from django.urls import path
from . import views

app_name = 'qa'
urlpatterns = [
	path('', views.index, name='index'),
	path('question/<int:question_id>/', views.question, name='question'),
	path('ask/', views.ask, name='ask'),
	path('popular/', views.popular, name='popular'),
	path('tagged/<slug:slug>/', views.tagged, name='tagged'),
	path('question_like/', views.question_like, name='question_like'),
	path('answer_like/', views.answer_like, name='answer_like'),
	path('answer_correct/', views.answer_correct, name='answer_correct'),
]

