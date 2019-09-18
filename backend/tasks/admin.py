from django.contrib import admin
from .models import Tasks

class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'complete', 'flair')


admin.site.register(Tasks, TasksAdmin)

# Register your models here.
