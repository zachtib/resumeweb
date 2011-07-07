from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.admin.models import User
from django.template import RequestContext

from resume.models import Degree, Job, Project, Skill, Extracurricular

def index(request, noheader=False):
    d = Degree.objects.all()
    j = Job.objects.all()
    p = Project.objects.all()
    s = Skill.objects.all()
    e = Extracurricular.objects.all()

    return render_to_response('index.html',
                                {   'degrees': d,
                                    'jobs': j,
                                    'projects': p,
                                    'skills': s,
                                    'extras': e,
                                })
