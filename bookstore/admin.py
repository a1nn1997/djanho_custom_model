from django.contrib import admin

from .models import Profile
# Register your models here.
# class BookStoreAdminArea(admin.AdminSite):
#     site_header = 'BookStore Admin Area'


# bookstore_site = BookStoreAdminArea(name='BookStoreAdmin')

class Filter(admin.ModelAdmin):
    list_display=('id','email','created_at','role','is_active')
    list_filter = ('is_active','created_at','role')

admin.site.register(Profile, Filter)