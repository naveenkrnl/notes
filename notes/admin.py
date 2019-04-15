from django.contrib import admin

# Register your models here.

from .models import NotesData

class NotesAdmin(admin.ModelAdmin):
    class meta:
        model=NotesData

admin.site.register(NotesData)