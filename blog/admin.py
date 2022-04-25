from dataclasses import field
from django.contrib import admin
from .models import Post,Category
# Register your models here.

#  part 1
class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog Admin Area'
    login_template = 'blog/admin/login.html'

blog_site = BlogAdminArea(name='BlogAdmin')

#admin.site.register(Post)

blog_site.register(Post)

#admin.site.register(Category)

blog_site.register(Category)
