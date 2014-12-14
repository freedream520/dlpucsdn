from django.contrib import admin
from account.models import profile,department

# Register your models here.
class profile_admin(admin.ModelAdmin):
    list_display = ('username','number','email','deleted','id')
class department_admin(admin.ModelAdmin):
    list_display = ('name','cn','id')
admin.site.register(profile,profile_admin)
admin.site.register(department,department_admin)
