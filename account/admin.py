from django.contrib import admin
from account.models import profile

# Register your models here.
class profile_admin(admin.ModelAdmin):
    list_display = ('username','number','email','deleted','id')
admin.site.register(profile,profile_admin)