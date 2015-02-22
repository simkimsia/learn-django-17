import logging

logger = logging.getLogger('reports.admin')

from django.contrib import admin

# Register your models here.
from reports.models import Report, ReportTemplate

class ReportAdmin(admin.ModelAdmin):
    fields = ['commodity', 
    'date',
    'trade_period',
    'quantity_cutoff',
    'data',
    'template',
    'title']

    actions = ['print_as_pdf']

    def print_as_pdf(self, request, queryset):
        logger.debug('anything')
        for report in queryset:
            markup = report.template.markup
            logger.debug(markup)
        return
    print_as_pdf.short_description = 'Generate as pdf'

admin.site.register(Report, ReportAdmin)
admin.site.register(ReportTemplate)
