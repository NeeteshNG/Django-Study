from django.contrib import admin
from service.models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_name', 'service_title', 'service_desc')

admin.site.register(Service, ServiceAdmin)