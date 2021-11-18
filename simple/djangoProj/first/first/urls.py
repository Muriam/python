from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('folder/', include('folder.urls')),
    path('admin/', admin.site.urls),
    
]
