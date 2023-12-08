from django.contrib import admin
from contact.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'subject')

admin.site.register(Contact, ContactAdmin)