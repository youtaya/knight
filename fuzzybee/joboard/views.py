# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from joboard.models import Factory
from joboard.forms import FactoryForm
from django.template import RequestContext

from urllib import urlopen, urlencode
import urllib2

from fuzzybee.conf import b_url, b_ak, geo_table, l_url, app_id, app_key
from utils.pack_json import toJSON, fromJSON

import logging
logger = logging.getLogger(__name__)

def index(request):
    form = None
    if request.method == 'POST':
        form = FactoryForm(request.POST)
        #print form
        if form.is_valid():
            factory = form.cleaned_data
            logger.debug("lat: " + str(factory['fact_lat']))
            logger.debug("addr: " + factory['fact_addr'])
            #save factory in model
            factmodel = form.save()
            factid = factmodel.id
            #save in public server: leancloud and baidu
            save_factory_cloud(factory)
            return HttpResponseRedirect(reverse('board:detail', args=(factid,)) )
    else:
        form = FactoryForm()
    return render_to_response('board/new.html', {'form': form}, context_instance=RequestContext(request))

def detail(request, fact_id):
    print fact_id
    info = get_object_or_404(Factory, pk=fact_id)
    return render(request, 'board/detail.html', {'info':info})

def save_factory_cloud(fact_info):
    title = fact_info['fact_name']
    address = fact_info['fact_addr']
    lat = fact_info['fact_lat']
    lng = fact_info['fact_lng']
    num = fact_info['hire_num']

    data = {
        'title': title.encode("utf-8"),
        'address': address.encode("utf-8"),
        'latitude': lat,
        'longitude': lng,
        'job_num': num,
        }
    head = {
        'X-AVOSCloud-Application-Id': app_id,
        'X-AVOSCloud-Application-Key': app_key,
        'Content-Type': 'application/json',
    }
    req = urllib2.Request(l_url, toJSON(data), head)
    print str(req)
    response = urllib2.urlopen(req)
    #print respone.read()
    lean_response = fromJSON(response.read())
    print lean_response

    lean_objectId = lean_response['objectId']
    # save in Baidu Map
    params = urlencode({
        'title': title.encode("utf-8"),
        'address': address.encode("utf-8"),
        'latitude': lat,
        'longitude': lng,
        'coord_type': 3,
        'geotable_id': geo_table,
        'ak': b_ak,
        'job_num': num,
        'lean_id': lean_objectId,
        })
    req = urllib2.Request(b_url, params)
    #print str(req)
    response = urllib2.urlopen(req)
    #print respone.read()
