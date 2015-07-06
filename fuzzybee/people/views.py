# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from people.models import People
from people.forms import SignupForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template import RequestContext
import logging
logger = logging.getLogger(__name__)

def signup_view(request):
    form = None
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print form
        if form.is_valid():
            signup = form.cleaned_data
            logger.debug("name: " + signup['username'])
            logger.debug("password: " + signup['password'])
            #save in user model
            user_model = form.save(commit=False)
            user_model.set_password(signup['password'])
            user_model.save()
            #save in people model
            people_model = People(user=user_model)
            people_model.save()

            return HttpResponseRedirect(reverse('people:login'))
    else:
        form = SignupForm()
    return render_to_response('people/signup.html', {'form': form}, context_instance=RequestContext(request))

def login_view(request):
    form = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        #print form
        if form.is_valid():

            username = request.POST.get('username', '')
            password = request.POST.get('password', '')

            print "name: " + username
            print "password: " + password

            user = authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    print "user active"
                    login(request, user)
                    return HttpResponseRedirect(reverse('board:manager'))
                else:
                    print "user not active"
                    return HttpResponse(404)
            else:
                print "user not exist"
                return HttpResponse(503)

    else:
        form = LoginForm()
    return render_to_response('people/login.html', {'form': form}, context_instance=RequestContext(request))

def logout_view(request):
    pass
    
def add_avatar(request):
    pass

def get_avatar(request):
    pass
