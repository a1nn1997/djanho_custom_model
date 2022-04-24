from dataclasses import field
from django.contrib import admin
from .models import Post,Category

# ( ) will bring the part in one line
TEXT = 'THIS IS TEXT'
class PostAdmin(admin.ModelAdmin):
    #fields=['title','author']
    #fields=['title',('author','slug')]
    fieldsets =(
        ('Section 1',{
            'fields': ('title','author',),
            'description': '%s' % TEXT,
        }),
        ('Section 2',{
            'fields': ('slug',),
            'classes':('collapse','wide',),
        })
    )

admin.site.register(Post, PostAdmin)

admin.site.register(Category)
