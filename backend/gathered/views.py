from django.shortcuts import render
from backend.serializers import EventSerializer
from .models import Event
from rest_framework import viewsets

# Create your views here.

class EventView(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

# Create your views here.
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')