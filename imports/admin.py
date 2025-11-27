from django.contrib import admin
from .models import Book, ImportJob

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'published_date')
    search_fields = ('title', 'author', 'isbn')

@admin.register(ImportJob)
class ImportJobAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    readonly_fields = ('errors', 'created_at')
