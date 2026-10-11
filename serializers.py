from rest_framework import serializers
from .models import Dog, Breed

class DogSerializer(serializers.Serializer):
id = serializers.IntegerField(read_only=True)
name = serializers.CharField(max_length=100)
breed = serializers.CharField(max_length=100)
age = serializers.IntegerField()