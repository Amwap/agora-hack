from django.contrib import admin
from apps.editor_app.models import Item, Project


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', ]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', ]
