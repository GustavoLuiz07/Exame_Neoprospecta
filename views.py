from django.shortcuts import render
from rest_framework import viewsets
from .models import Backend_Developer, Frontend_Developer
from .serializers import Backend_DeveloperSerializer, Frontend_DeveloperSerializer

class Backend_DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Backend_Developer.objects.all()
    serializer_class = Backend_DeveloperSerializer

class Frontend_DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Frontend_Developer.objects.all()
    serializer_class = Frontend_DeveloperSerializer
