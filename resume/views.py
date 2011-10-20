from django.shortcuts import render_to_response

from resume.models import *

def index(request):
    try:
        ip = request.get_host()
        visitor = Visitor.objects.all().filter(ipaddress=ip)
        if len(visitor) != 1:
            visitor = Visitor()
            visitor.ipaddress = ip
            visitor.save()
        else:
            visitor = visitor[0]
            visitor.visits += 1
            visitor.save()
    except:
        pass
    
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

    return render_to_response('index.html', locals())


