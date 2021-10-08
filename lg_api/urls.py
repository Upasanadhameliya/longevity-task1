"""
lg_api URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include # noqa
from rest_framework.authtoken import views

from .documentation import documentation_url

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path('auth/', views.obtain_auth_token),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + documentation_url
)

admin.site.site_header = "{} administration".format(settings.PROJECT_NAME)
admin.site.site_title = "{} administration".format(settings.PROJECT_NAME)
admin.site.site_url = "{}".format(settings.PROJECT_URL)
admin.site.index_title = "{} administration".format(settings.PROJECT_NAME)
admin.empty_value_display = "**Empty**"
