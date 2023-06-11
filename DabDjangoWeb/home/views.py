from django.shortcuts import render, HttpResponse, redirect
from home.models import Users
from django.contrib.sessions.models import Session
from django.utils.crypto import get_random_string
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from django.contrib.auth.models import User
from google_auth_oauthlib.flow import InstalledAppFlow
from django.conf import settings
import json
import logging
from google.oauth2 import id_token
from google.auth.transport import requests
from django.http import HttpResponseBadRequest
from datetime import datetime


# Create your views here.


def home(request):
    return render(request, 'my_index.html')


def submit_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_user = Users(user_name=username, third_party_name='Google')
        new_user.save()
        return redirect('/home')


def create_unique_session_key():
    while True:
        key = get_random_string(length=32)
        if not Session.objects.filter(session_key=key).exists():
            return key


def custom_login(request, user):
    if user:
        request.session.flush()  
        request.session.create()  
        request.session.session_key = create_unique_session_key()
        request.session.modified = True
        request.session['user_id'] = user.id  # Store user ID in the session
    else:
        pass


def logout(request):
    request.session.flush()
    return redirect('/home')


logger = logging.getLogger(__name__)

def google_login(request):
    flow = Flow.from_client_config(
        client_config=settings.GOOGLE_OAUTH2_CONFIG,
        scopes=["openid", "https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email"],
        redirect_uri=request.build_absolute_uri(reverse('google-callback')),
    )
    authorization_url, state = flow.authorization_url()
    request.session['state'] = state
    return HttpResponseRedirect(authorization_url)


def google_callback(request):
    state = request.session['state']
    print(state)
    flow = Flow.from_client_config(
        client_config=settings.GOOGLE_OAUTH2_CONFIG,
        scopes=["openid", "https://www.googleapis.com/auth/userinfo.profile",
                "https://www.googleapis.com/auth/userinfo.email"],
        redirect_uri=request.build_absolute_uri(reverse('google-callback')),
        
    )
    flow.fetch_token(authorization_response=request.build_absolute_uri())

    credential = flow.credentials
    print("Google OAuth session expires at:", credential.expiry)
    service = build('oauth2', 'v2', credentials=credential)
    profile = service.userinfo().get().execute()
    print("User name:", profile['name'])
    print("Email:", profile['email'])

    email = profile['email']
    name = profile['name']

    user, _ = User.objects.get_or_create(
        username=email, defaults={'email': email, 'first_name': name})
    
    

    login(request, user)
    request.session['expiry_time'] = str(credential.expiry)
    remaining_time = (credential.expiry - datetime.utcnow()).total_seconds()
    # Update the session's expiry date to match the Google OAuth session's expiry date
    request.session.set_expiry(remaining_time)


    return HttpResponseRedirect(reverse('home'))  # Redirect to the homepage
