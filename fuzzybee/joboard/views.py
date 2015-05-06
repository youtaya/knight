from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from joboard.models import Factory
from joboard.forms import FactoryForm
from django.template import RequestContext

from urllib import urlopen, urlencode
import urllib2

import logging
logger = logging.getLogger(__name__)

url = "http://api.map.baidu.com/geodata/v2/poi/create"
ak = "XOyqpuhcxMxuHjpUr4T2BIOG"
geo_table = "100729"

def index(request):
    form = None
    if request.method == 'POST':
        form = FactoryForm(request.POST)
        if form.is_valid():
            factory = form.cleaned_data
            logger.debug("lat: " + str(factory['fact_lat']))
            logger.debug("lng: " + str(factory['fact_lng']))
            # TODO: save factory in model
            create_poi(factory)
            return HttpResponseRedirect(reverse('board:detail'))
    else:
        form = FactoryForm()
    return render_to_response('board/new.html', {'form': form}, context_instance=RequestContext(request))

def detail(request):
    #create_poi()
    return render(request, 'board/detail.html')

def create_poi(fact_info):
    title = "test factory"
    address = fact_info['fact_addr']
    lat = fact_info['fact_lat']
    lng = fact_info['fact_lng']
    
    params = urlencode({
        'title': title,
        'address': address
        'latitude': lat,
        'longitude': lng,
        'coord_type': 3,
        'geotable_id': geo_table,
        'ak': ak
        })
    req = urllib2.Request(url, params)
    print str(req)
    respone = urllib2.urlopen(req)
    print respone.read()
