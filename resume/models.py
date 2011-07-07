from django.contrib.auth.models import User
from django.db import models

class Resume(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField('Full Name', max_length=200)
    objective = models.TextField()

    def __unicode__(self):
        return 'Resume for %s' % self.name

class Degree(models.Model):
    resume = models.ForeignKey(Resume)
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    graddate = models.DateField('Graduation Date')

class Job(models.Model):
    resume = models.ForeignKey(Resume)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    startdate = models.DateField('Start Date')
    enddate = models.DateField('End Date', null=True, blank=True)
    description = models.TextField()

class Project(models.Model):
    resume = models.ForeignKey(Resume)
    name = models.CharField(max_length=200)
    begindate = models.DateField('Begin Date')
    enddate = models.DateField('End Date', null=True, blank=True)
    description = models.TextField()

class Skill(models.Model):
    resume = models.ForeignKey(Resume)
    title = models.CharField(max_length=200)
    description = models.TextField()

class Extracurricular(models.Model):
    resume = models.ForeignKey(Resume)
    begindate = models.DateField('Begin Date')
    enddate = models.DateField('End Date', null=True, blank=True)
    description = models.CharField(max_length=200)
