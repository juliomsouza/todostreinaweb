from django.contrib import admin
from todos.models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "deadline", "finished_at")
    list_filter = ("title",)
