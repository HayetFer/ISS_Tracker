from django.contrib import admin

from polls.models import Bienvenue

# Register your models here.

class MyAdmin(admin.ModelAdmin):
    list_display = ('mail',)

admin.site.register(Bienvenue, MyAdmin)
