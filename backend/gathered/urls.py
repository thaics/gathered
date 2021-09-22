from django.urls import path, include
from gathered import views
from .views import index

urlpatterns = [
    path('', index, name=''),
    path('content', index),
]