from django.contrib import admin
from .models import* 
from .models import MediaItem

admin.site.register(register)



@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'subtitle')
