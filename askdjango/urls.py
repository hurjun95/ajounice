
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path(r'admin/', admin.site.urls),
    re_path(r'^blog/', include('blog.urls')),
    re_path(r'^dojo/', include('dojo.urls'))
]
