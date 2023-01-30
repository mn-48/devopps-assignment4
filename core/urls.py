"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from graphene_django.views import GraphQLView
from graphene_file_upload.django import FileUploadGraphQLView
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from ckeditor_uploader import views as ckeditor_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('iportfolio.urls')),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('ckeditor/upload/', login_required(ckeditor_views.upload),
         name='ckeditor_upload'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # new

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)
