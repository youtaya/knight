from django.shortcuts import render
from django.http import HttpResponse

import logging
logger = logging.getLogger(__name__)

def applysync(request):
    data = {}

    if request.method == 'POST':
        logger.debug(str(request.POST))

        fact_id = request.POST.get('factory_id')
        empolyee_name = request.POST.get('name')
        job_position = request.POST.get('job_postion')
        factory = Factory.objects.get(id=fact_id)

        resume = Resume(apply_factory=factory)
        resume.name = empolyee_name
        resume.apply_job = job_position

        resume.save()

        return HttpResponse(200)
