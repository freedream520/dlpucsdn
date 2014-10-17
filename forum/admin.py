from django.contrib import admin
from forum.models import topic
# Register your models here.
class forum_admin(admin.ModelAdmin):
    list_display = ('title','auth','time_created','reply_count','id')
admin.site.register(topic,forum_admin)