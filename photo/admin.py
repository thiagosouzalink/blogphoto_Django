from django.contrib import admin

from .models import Photo

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = ['photo_user', 'created_at', 'photo_url']
    list_display_links = ['photo_user', 'photo_url']
