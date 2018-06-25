from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.i18n import JavaScriptCatalog

js_info_dict = {
    'packages': ['recurrence'],
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testapp/', include('testapp.urls')),
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), js_info_dict),
]
