from dataclasses import field
from django.contrib import admin
from .models import Post,Category
from django import forms
#this is part 1 using fields and fieldsets

    # ( ) will bring the part in one line
    # TEXT = 'THIS IS TEXT'
# class PostAdmin(admin.ModelAdmin):
#     #fields=['title','author']
#     #fields=['title',('author','slug')]
#     fieldsets =(
#         ('Section 1',{
#             'fields': ('title','author',),
#             'description': '%s' % TEXT,
#         }),
#         ('Section 2',{
#             'fields': ('slug',),
#             'classes':('collapse','wide',),
#         })
#     )

# this part 2 using forms

class PostForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(PostForm, self).__init__(*args,**kwargs)
        self.fields['title'].help_text = 'New Help Text'
    
    class Meta:
        model=Post
        exclude=('slug',)

class PostFormAdmin(admin.ModelAdmin):
    form=PostForm


admin.site.register(Post, PostFormAdmin)

admin.site.register(Category)
