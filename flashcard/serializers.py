from rest_framework import serializers
from .models import Prompt,Wikipedia




class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = ['id', 'Prompt_title', 'Prompt', 'Wikipedia_link', 'Code', 'Summary', 'User','mcq', 'created_at']
        read_only_fields = ['id', 'created_at']
        extra_kwargs = {
            'Prompt_title': {'required': False, 'allow_null': True},
            'Prompt': {'required': False, 'allow_null': True},
            'Code': {'required': False, 'allow_null': True},
            'Summary': {'required': False, 'allow_null': True},
            'User': {'required': False, 'allow_null': True},
            'mcq': {'required': False, 'allow_null': True}
        }



class WikipediaSerializer(serializers.ModelSerializer):
    code_avaliable = serializers.SerializerMethodField()
    available_codes = serializers.SerializerMethodField()

    class Meta:
        model = Wikipedia
        fields = ['id', 'wikipedia_url', 'slug','mermaid_Code', 'p5_code', 'three_Code', 'd3_code', 'summary','mcq','code_avaliable', 'available_codes']

    def get_code_avaliable(self, obj):
        return bool(obj.wikipedia_url and (obj.mermaid_Code or obj.p5_code or obj.three_Code or obj.d3_code))

    def get_available_codes(self, obj):
        available_codes = []
        if obj.mermaid_Code:
            available_codes.append("Mermaid")
        if obj.p5_code:
            available_codes.append("p5.js")
        if obj.three_Code:
            available_codes.append("Three.js")
        if obj.d3_code:
            available_codes.append("D3.js")
        return available_codes

       
