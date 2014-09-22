from django.contrib import admin
from home.models import Topic

# Register your models here.
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','address','city')
    search_fields = ('name','city')

admin.site.register(Topic)
