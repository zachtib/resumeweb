from django.shortcuts import render_to_response

from resume.models import Degree, Job, Project, Skill, Extracurricular

def index(request):
    degrees = Degree.objects.all()
    jobs = Job.objects.all()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    extras = Extracurricular.objects.all()

    return render_to_response('index.html', locals())


