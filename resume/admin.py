from resume.models import *
from django.contrib import admin


class DateRangeInline(admin.TabularInline):
    model = DateRange
    fields = ['start', 'end',]
    extra = 1

class BasicInformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email',)
    fieldsets = [
        (None,      {'fields': ['name', 'phone', 'email', 'objective',]})
    ]

class DegreeAdmin(admin.ModelAdmin):
    list_display = ('degree', 'school',)
    fieldsets = [
        (None,      {'fields': ['degree', 'school', 'graddate',]}),
        ('Config',  {'fields': ['order',]}),
    ]

class JobAdmin(admin.ModelAdmin):
    list_display = ('company', 'position',)
    fieldsets = [
        (None,      {'fields': ['company', 'position', 'location', 'description',]}),
        ('Config',  {'fields': ['order',]}),
    ]
    inlines = [DateRangeInline]

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldsets = [
        (None,      {'fields': ['name', 'description', 'link',]}),
        ('Config',  {'fields': ['order',]}),
    ]
    inlines = [DateRangeInline]

class SkillAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fieldsets = [
        (None,      {'fields': ['title', 'description',]}),
        ('Config',  {'fields': ['order',]}),
    ]

class ExtracurricularAdmin(admin.ModelAdmin):
    list_display = ('description',)
    fieldsets = [
        (None,      {'fields': ['description',]}),
        ('Config',  {'fields': ['order',]}),
    ]
    inlines = [DateRangeInline]

class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ipaddress', 'visits', 'lastvisit',)

admin.site.register(BasicInformation, BasicInformationAdmin)
admin.site.register(Degree, DegreeAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Extracurricular, ExtracurricularAdmin)
admin.site.register(Visitor, VisitorAdmin)



