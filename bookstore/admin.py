from django.contrib import admin

from . import models
# Register your models here.
class BookStoreAdminArea(admin.AdminSite):
    site_header = 'BookStore Admin Area'


bookstore_site = BookStoreAdminArea(name='BookStoreAdmin')
