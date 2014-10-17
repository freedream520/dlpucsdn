from django.contrib import admin
from news.models import list

# Register your models here.
class news_admin(admin.ModelAdmin):
    list_display = ('title','auth','url','time_created','department_name','id')

admin.site.register(list,news_admin)