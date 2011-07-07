from resume.models import *
from django.contrib import admin


class DateRangeInline(admin.TabularInline):
    model = DateRange
    fields = ['start', 'end']
    extra = 1

class DateInlineAdmin(admin.ModelAdmin):
    inlines = [DateRangeInline, ]

admin.site.register(BasicInformation)
admin.site.register(Degree)
admin.site.register(Job, DateInlineAdmin)
admin.site.register(Project, DateInlineAdmin)
admin.site.register(Skill)
admin.site.register(Extracurricular, DateInlineAdmin)



