from rest_framework import serializers
from .models import Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'title', 'description', 'column', 'position', 'due_date', 'created_at', 'updated_at']
