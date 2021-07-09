
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gathered.urls', namespace='gathered')),
    path('api/', include('gathered_api.urls', namespace='gathered_api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
