from rest_framework import serializers
from .models import Prompt, PromptGroup

class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = ('id', 'name','audio_file','tags')

class PromptGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromptGroup
        fields = ('id', 'name','tag','position','is_active')