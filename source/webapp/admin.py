from django.contrib import admin
from webapp.models import Issue, Status, Type, Project


class IssueAdmin(admin.ModelAdmin):
    list_display = ['pk', 'summary', 'status', 'type', 'created_at']
    list_filter = ['status', 'type']
    list_display_links = ['pk', 'summary']
    search_fields = ['summary', 'description']
    readonly_fields = ['created_at']
    exclude = []


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'description', 'created_at', 'updated_at']
    list_filter = ['name']
    list_display_links = ['pk', 'name']
    search_fields = ['name']
    readonly_fields = ['created_at', 'updated_at']
    exclude = []


class StatusAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ['status_name']
    list_filter = ['status_name']
    list_display_links = ['status_name']
    search_fields = ['status_name']


class TypeAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ['type_name']
    list_filter = ['type_name']
    list_display_links = ['type_name']
    search_fields = ['type_name']


admin.site.register(Issue, IssueAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Type, TypeAdmin)