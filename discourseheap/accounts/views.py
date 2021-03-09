import urllib
import json
import os
from . import forms
import random
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse

"""
def send_activation_email(user):
    subject = '...'
    message = 'Hi ' + str(user.username) + ',\n\nHere is the activate code to unlock your account ' + str(user.profile.activation_code) + '.\n\nThanks,\n...'
    email_from = settings.EMAIL_HOST_USER
    send_mail( subject, message, email_from, [user.email,], fail_silently=False)

def activate_account(request):
    try:
        code = int(request.GET.get('activation_code', ""))
        if (code == request.user.profile.activation_code):
            request.user.profile.email_confirmed = True
            request.user.profile.save()
            data = {"validated":True,"message":"Account activated!"}
        else:
            data = {"validated":False,"message":"Incorrect code"}
    except:
        data = {"validated":False,"message":"Code must be 4 numbers"}
    
    return JsonResponse(data)
"""

def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            # Add email activation here in needed

            return redirect('home')
    else:
        form = forms.SignUpForm()
    return render(request, 'signup.html', {"form": form})

def login_user(request):
    if request.method == "POST":
        form = forms.UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return render(request, 'login.html', {"form": form})
        else:
            return render(request, "login.html", {"form":form, "error_msg":"Incorrect username or password"})
    else:
        form = forms.UserLoginForm
        return render(request, "login.html", {"form": form})