from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('testapp.urls')),
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript_catalog'),
]
