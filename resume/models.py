from django.db import models

class BasicInformation(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    objective = models.TextField()

    def __unicode__(self):
        return self.name

class Degree(models.Model):
    order = models.IntegerField(unique=True)
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    graddate = models.DateField('Graduation Date')

    def __unicode__(self):
        return self.degree

class Job(models.Model):
    order = models.IntegerField(unique=True)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.company

class Project(models.Model):
    order = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    link = models.CharField(max_length=1000, null=True, blank=True)

    def __unicode__(self):
        return self.name

class Skill(models.Model):
    order = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.title

class Extracurricular(models.Model):
    order = models.IntegerField(unique=True)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.description

class DateRange(models.Model):
    job = models.ForeignKey(Job, null=True)
    project = models.ForeignKey(Project, null=True)
    extra = models.ForeignKey(Extracurricular, null=True)
    start = models.DateField('Start Date')
    end = models.DateField('End Date', null=True, blank=True)

    def __unicode__(self):
        if self.end is None:
            return '%s to Present' % (self.start.strftime("%B %e, %Y"))
        else:
            return '%s to %s' % (self.start.strftime("%B %e, %Y"), self.end.strftime("%B %e, %Y"))

class Visitor(models.Model):
    ipaddress = models.IPAddressField(primary_key=True, editable=False)
    visits = models.IntegerField(default=1, editable=False)
    lastvisit = models.DateField(auto_now=True, editable=False)
    
    def __unicode__(self):
        return self.ipaddress
