from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PromptSerializer, PromptGroupSerializer
from .models import Prompt, PromptGroup

# Create your views here.

class PromptView(viewsets.ModelViewSet):
    serializer_class = PromptSerializer
    queryset = Prompt.objects.all()

class PromptGroupView(viewsets.ModelViewSet):
    serializer_class = PromptGroupSerializer
    queryset = PromptGroup.objects.all()