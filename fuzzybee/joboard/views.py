from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from joboard.models import Factory
from joboard.forms import FactoryForm
from django.template import RequestContext

import logging
logger = logging.getLogger(__name__)

def index(request):
    form = None
    if request.method == 'POST':
        form = FactoryForm(request.POST)
        if form.is_valid():
            factory = form.cleaned_data
            logger.debug("name: " + factory['fact_name'])
            logger.debug("address: " + factory['fact_addr'])
            return HttpResponseRedirect(reverse('board:detail'))
    else:
        form = FactoryForm()
    return render_to_response('board/new.html', {'form': form}, context_instance=RequestContext(request))

def detail(request):
    return render(request, 'board/detail.html')
