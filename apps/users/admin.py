from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = (
        'username',
        'timezone',
        'language',
    )
    list_display = (
        'id',
        'username',
    )
    list_display_links = (
        'id',
        'username',
    )
