#URLs for app 'users'

from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
	path('', include('django.contrib.auth.urls')),
	path('signup/', views.signup, name='signup'),
	path('settings/', views.show_profile, name='show_profile'),
	path('settings/update/', views.update_profile, name='update_profile'),
]