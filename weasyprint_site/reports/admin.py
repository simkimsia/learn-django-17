from django.contrib import admin

# Register your models here.
from reports.models import Report, ReportTemplate

def print_as_pdf(modeladmin, request, queryset):
	return

print_as_pdf.short_description = "Generate pdf"

class ReportAdmin(admin.ModelAdmin):
    fields = ['commodity', 
    'date',
    'trade_period',
    'quantity_cutoff',
    'data',
    'template',
    'title']
    actions = [print_as_pdf]

admin.site.register(Report, ReportAdmin)
admin.site.register(ReportTemplate)
