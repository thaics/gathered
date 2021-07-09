from django.urls import path, include
from django.views.generic import TemplateView

app_name = 'gathered'

urlpatterns = [
    path('', TemplateView.as_view(template_name="gathered/index.html")),
]
