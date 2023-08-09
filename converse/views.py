from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PromptSerializer, PromptGroupSerializer, ScenarioSerializer
from .models import Prompt, PromptGroup, Scenario

# Create your views here.

class PromptView(viewsets.ModelViewSet):
    serializer_class = PromptSerializer
    queryset = Prompt.objects.all()

class PromptGroupView(viewsets.ModelViewSet):
    serializer_class = PromptGroupSerializer
    queryset = PromptGroup.objects.all()

class ScenarioView(viewsets.ModelViewSet):
    serializer_class = ScenarioSerializer
    queryset = Scenario.objects.all()