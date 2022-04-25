from dataclasses import field
from django.contrib import admin
from .models import Post,Category
from  django_summernote.admin import SummernoteModelAdmin
# Register your models here.

#  part 1
class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog Admin Area'
    login_template = 'blog/admin/login.html'

blog_site = BlogAdminArea(name='BlogAdmin')

class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'



admin.site.register(Post , SummerAdmin)

blog_site.register(Post , SummerAdmin)

#admin.site.register(Category)

blog_site.register(Category)
