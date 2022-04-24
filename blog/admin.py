from dataclasses import field
from django.contrib import admin
from .models import Post,Category
# Register your models here.

#  part 1
# class BlogAdminArea(admin.AdminSite):
#     site_header = 'Blog Admin Area'


# blog_site = BlogAdminArea(name='BlogAdmin')

# admin.site.register(models.Post)

# blog_site.register(models.Post)

# admin.site.register(models.Category)

# blog_site.register(models.Category)

# part 2

    # way 1
# class PostAdmin(admin.ModelAdmin):
#     fields=['title','author']

# admin.site.register(Post, PostAdmin)

    #way 2
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields=['title','author']

#admin.site.register(Post, PostAdmin)

