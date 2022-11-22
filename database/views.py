from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SignUpForm, LogInForm
from .models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
import json, os
from spotipy import oauth2
import spotipy
from spotipy import SpotifyOAuth
from urllib.parse import urlparse, parse_qs

def index(request):
    return HttpResponse("Database Project Lies Ahead")

def signUp(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #Task: make sure username is not taken
            username = form.cleaned_data['username']

            #salt and hash password
            pword = make_password(form.cleaned_data['password'])
            ageGiven = form.cleaned_data['age']
            newUser = User(userID = username, password = pword, age=ageGiven)
            newUser.save()
            #redirect to link spotify auth form
            return HttpResponseRedirect('log-in/')

    # if a GET (or any other method) we'll create a blank form
    else:
        context = {}
        context['form'] = SignUpForm()
        return render(request, 'sign-up.html', context)

def logIn(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LogInForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #need to authenticate 
            
            #first find row with the given username
            name = form.cleaned_data['username']
            
            #find user
            query = User.objects.get(userID=name)

            if(check_password(form.cleaned_data['password'], query.password)):
                return HttpResponseRedirect('home/')
            else:
                #redirect to same page and render error
                print('WRONG USERNAME OR PASSWORD')
                return HttpResponseRedirect('log-in/')

    # if a GET (or any other method) we'll create a blank form
    else:
        context = {}
        context['form'] = LogInForm()
        return render(request, 'login.html', context)

def home(request):
    return HttpResponse("This is the homepage")