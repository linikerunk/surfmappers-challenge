from django.contrib import admin
from .models import GaleryPhoto


@admin.register(GaleryPhoto)
class GaleryPhotoAdmin(admin.ModelAdmin):
    list_display = ('name','description', 'image_date', 'approved')
    list_editable = ('approved', )
    list_display_link = ('id', 'name',)
