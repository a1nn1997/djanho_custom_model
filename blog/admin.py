from dataclasses import field
from django.contrib import admin
from .models import Post,Category

# ( ) will bring the part in one line

class PostAdmin(admin.ModelAdmin):
    #fields=['title','author']
    fields=['title',('author','slug')]

admin.site.register(Post, PostAdmin)

admin.site.register(Category)
