# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from people.models import People
from people.forms import SignupForm
from django.template import RequestContext
import logging
logger = logging.getLogger(__name__)

def signup(request):
    form = None
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print form
        if form.is_valid():
            signup = form.cleaned_data
            logger.debug("name: " + signup['username'])
            logger.debug("password: " + signup['password'])
            #save in user model
            user_model = form.save()

            return HttpResponseRedirect(reverse('people:login'))
    else:
        form = SignupForm()
    return render_to_response('people/signup.html', {'form': form}, context_instance=RequestContext(request))

def login(request):
    form = None
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print form
        if form.is_valid():
            signup = form.cleaned_data
            logger.debug("name: " + signup['username'])
            logger.debug("password: " + signup['password'])

            user_name = signup['username']
            password = signup['password']
            user = User.objects.filter(username = user_name,password = password)

            if user:
                HttpResponseRedirect(reverse('joboard:detail'))
    else:
        form = SignupForm()
    return render_to_response('people/login.html', {'form': form}, context_instance=RequestContext(request))


def add_avatar(request):
    pass

def get_avatar(request):
    pass
