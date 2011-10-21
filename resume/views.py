from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import get_template
from resume.models import *

import StringIO
import ho.pisa as pisa
import logging

class PisaNullHandler(logging.Handler):
    def emit(self, record):
        pass

logging.getLogger("ho.pisa").addHandler(PisaNullHandler())


def index(request):
    basic = BasicInformation.objects.all()
    if len(basic) != 1:
        raise Exception(
            'Error: You must have exactly ONE BasicInformation object')
    basic = basic[0]
    degrees = Degree.objects.all().order_by('order')
    jobs = Job.objects.all().order_by('order')
    projects = Project.objects.all().order_by('order')
    skills = Skill.objects.all().order_by('order')
    extras = Extracurricular.objects.all().order_by('order')

    for job in jobs:
        job.dates = DateRange.objects.filter(job=job)
    for project in projects:
        project.dates = DateRange.objects.filter(project=project)
    for extra in extras:
        extra.dates = DateRange.objects.filter(extra=extra)
    
    pdf = False
    if request.method == "GET" and "pdf" in request.GET:
        pdf = True
    
    context = RequestContext(request, locals())
    template = get_template("index.html")
    html = template.render(context)
    result = StringIO.StringIO()
    if pdf:
        pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
        response = HttpResponse(mimetype="application/pdf")
        response['Content-Disposition'] = 'attachment; Resume.pdf'
        response.write(result.getvalue())
        return response

    return render_to_response('index.html', locals())


