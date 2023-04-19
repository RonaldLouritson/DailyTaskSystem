from django.contrib import admin
from .models import Category, JobIssue, Note

class NoteInline(admin.StackedInline):
    model = Note
    extra = 0

class JobIssueAdmin(admin.ModelAdmin):
    # inlines = [
    #     NoteInline,
    # ]
    list_display = ('category', 'title', 'date_created')
    list_filter = ('category', 'date_created')
    search_fields = ('category', 'title', 'description')
    readonly_fields = ('date_created', 'date_updated')
    fieldsets = (
        (None, {'fields': ('title', 'category', 'description')}),
        ('Dates', {'fields': ('date_created', 'date_updated'), 'classes': ('collapse',)}),
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class NoteAdmin(admin.ModelAdmin):
    list_display = ('job_issue', 'content')
    search_fields = ('job_issue__title', 'content')

admin.site.register(Category, CategoryAdmin)
admin.site.register(JobIssue, JobIssueAdmin)
admin.site.register(Note, NoteAdmin)
