from django.contrib import admin
from blog.models import blogs
# Register your models here.
class blog_admin(admin.ModelAdmin):
    list_display = ('title','auth','time_created','id')
admin.site.register(blogs,blog_admin)