from django.contrib import admin
from django.urls import path, include 
# Including api points for djoser(for creating users)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
]
