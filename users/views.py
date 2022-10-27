from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
def signup(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('qa:index')
    context = {'form': form}
    return render(request, 'signup.html', context)

@login_required
def show_profile(request):
    user=request.user
    profile = get_object_or_404(Profile, user=request.user)
    context = {'user': user, 'profile': profile}
    return render(request, 'show_profile.html', context)

@login_required
def update_profile(request):
    if request.method != 'POST':
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    else:
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('users:show_profile')
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'update_profile.html', context)
