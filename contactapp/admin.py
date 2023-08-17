from django.contrib import admin
from .models import Contact
# admin.site.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('id','Name','phoneno',)

    ordering=('Name',)
    search_fields=('Name','phoneno')
admin.site.register(Contact,ContactAdmin)



