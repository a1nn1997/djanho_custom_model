"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.admin import blog_site
#from bookstore.admin import bookstore_site
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin1/', blog_site.urls),
    #path('admin2/', bookstore_site.urls),
    path('',include('blog.urls',namespace='blog')),
    path('summernote/', include('django_summernote.urls')),    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

#admin.site.index_title= "django index title"
#admin.site.site_header= "site header"
#admin.site.site_title= "site title"

