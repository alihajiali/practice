from django import forms
from django.shortcuts import render, redirect
from .forms import login_form, register_form
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("post:all_post")
    else:
        form = login_form()
    return render(request, 'accounts/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = register_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            login(request, user)
            return redirect("post:all_post")
    else:
        form = register_form()
    return render(request, 'accounts/register.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect("post:all_post")