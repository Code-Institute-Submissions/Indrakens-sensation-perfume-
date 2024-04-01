from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Add contact to admin panel"""
    list_display = ('email', 'query', 'subject', 'message')
    list_filter = ('query', 'email')
    search_fields = ('query', 'email')
