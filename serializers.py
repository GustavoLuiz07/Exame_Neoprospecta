from rest_framework import serializers
from .models import Backend_Developer, Frontend_Developer

class Backend_DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backend_Developer
        fields = ('id', 'name', 'contribution', 'years_old', 'special_needs')
        fields = '__all__'

class Frontend_DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frontend_Developer
        fields = ('id', 'name', 'contribution', 'years_old', 'special_needs')
        fields = '__all__'
