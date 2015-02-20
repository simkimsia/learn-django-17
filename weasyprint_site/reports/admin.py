from django.contrib import admin

# Register your models here.
from reports.models import Report, ReportTemplate

class ReportAdmin(admin.ModelAdmin):
    fields = ['commodity', 
    'date',
    'trade_period',
    'quantity_cutoff',
    'title']

admin.site.register(Report, ReportAdmin)
admin.site.register(ReportTemplate)
