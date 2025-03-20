from rest_framework import serializers
from .models import Prompt

# class PromptSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Prompt
#         fields = ['id', 'Prompt_title', 'Prompt', 'Wikipedia_link', 'Code', 'Summary', 'User','created_at']
#         read_only_fields = ['id', 'created_at']


from rest_framework import serializers
from .models import Prompt

class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = ['id', 'Prompt_title', 'Prompt', 'Wikipedia_link', 'Code', 'Summary', 'User', 'created_at']
        read_only_fields = ['id', 'created_at']
        extra_kwargs = {
            'Prompt_title': {'required': False, 'allow_null': True},
            'Prompt': {'required': False, 'allow_null': True},
            'Code': {'required': False, 'allow_null': True},
            'Summary': {'required': False, 'allow_null': True},
            'User': {'required': False, 'allow_null': True}
        }

