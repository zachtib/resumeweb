from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db import models

class ContactInformation(models.Model):
    site = models.OneToOneField(Site)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    objective = models.TextField()

    def __unicode__(self):
        return self.name


class DateRange(models.Model):
    start = models.DateField('Start Date')
    end = models.DateField('End Date')

class Degree(models.Model):
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    graddate = models.DateField('Graduation Date')

class Job(models.Model):
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    startdate = models.DateField('Start Date')
    enddate = models.DateField('End Date', null=True, blank=True)
    description = models.TextField()

class Project(models.Model):
    name = models.CharField(max_length=200)
    begindate = models.DateField('Begin Date')
    enddate = models.DateField('End Date', null=True, blank=True)
    description = models.TextField()

class Skill(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

class Extracurricular(models.Model):
    begindate = models.DateField('Begin Date')
    enddate = models.DateField('End Date', null=True, blank=True)
    description = models.CharField(max_length=200)
