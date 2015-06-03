from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
from resume.models import Resume
from resume.forms import ResumeForm
from joboard.models import Factory

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

def applylist(request):
    #TODO: hard code 1
    fact_id = 1
    factory = Factory.objects.get(id=fact_id)
    resumes = Resume.objects.filter(apply_factory=factory)
    relist = [ResumeForm(model_to_dict(resume)) for resume in resumes]

    return render(request, 'resume/list.html', {'relist':relist})

def applyid(request, fact_id):
    factory = Factory.objects.get(id=fact_id)
    resumes = Resume.objects.filter(apply_factory=factory)
    relist = [ResumeForm(model_to_dict(resume)) for resume in resumes]

    return render(request, 'resume/list.html', {'relist':relist})
