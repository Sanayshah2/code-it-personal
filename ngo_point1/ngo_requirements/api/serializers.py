from rest_framework import serializers
from ngo_requirements.models import *

class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = [
            'pk',
            'requirement_heading',
            'requirement_content',
            'category',
            'quantity',
            'amount',
            'requirement_fulfilled', 
        ]
        read_only_fields = ['pk']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Help_category
        fields = [
            'pk',
            'help_category', 
        ]
        read_only_fields = ['pk']
