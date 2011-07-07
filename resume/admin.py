from resume.models import Resume, Degree, Job, Project, Skill, Extracurricular
from django.contrib import admin

class DegreeInline(admin.StackedInline):
    model = Degree
    extra = 1

class JobInline(admin.StackedInline):
    model = Job
    extra = 1

class ProjectInline(admin.StackedInline):
    model = Project
    extra = 1

class SkillInline(admin.StackedInline):
    model = Skill
    extra = 1

class ExtracurricularInline(admin.TabularInline):
    fields = ['description', 'begindate', 'enddate']
    model = Extracurricular
    extra = 1

class ResumeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General', {'fields': ['user', 'name', 'objective']})
    ]
    inlines = [DegreeInline, JobInline, ProjectInline, SkillInline,
        ExtracurricularInline]

admin.site.register(Resume, ResumeAdmin)

