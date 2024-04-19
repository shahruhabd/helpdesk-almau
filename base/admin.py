from django.contrib import admin
from base.models import *

@admin.register(HelpDeskRequest)
class HelpDeskRequestAdmin(admin.ModelAdmin):
    list_display = ['creator', 'auditorium_number', 'description', 'handler', 'status', 'created_at']
    search_fields = ['creator__full_name', 'auditorium_number', 'description', 'handler__username']

admin.site.register(Lecturer)
admin.site.register(HelpDeskUser)

