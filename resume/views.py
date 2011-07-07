from django.shortcuts import render_to_response

from resume.models import *

def index(request):
    basic = BasicInformation.objects.all()
    if len(basic) != 1:
        raise Exception(
            'Error: You must have exactly ONE BasicInformation object')
    basic = basic[0]
    degrees = Degree.objects.all()
    jobs = Job.objects.all()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    extras = Extracurricular.objects.all()

    for job in jobs:
        job.dates = DateRange.objects.filter(job=job)
    for project in projects:
        project.dates = DateRange.objects.filter(project=project)
    for extra in extras:
        extra.dates = DateRange.objects.filter(extra=extra)

    return render_to_response('index.html', locals())


