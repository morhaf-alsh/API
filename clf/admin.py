from django.contrib import admin
from .models import entries

# Register your models here.
class entryAdmin(admin.ModelAdmin):
    list_display = ['the_kind']
admin.site.register(entries,entryAdmin)