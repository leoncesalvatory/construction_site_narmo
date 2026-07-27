from django.contrib import admin
from .models import *

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tagline')

admin.site.register(Certification)
admin.site.register(TeamMember)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(NewsPost)
admin.site.register(JobPosting)
admin.site.register(CompanyLogo)
@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email')