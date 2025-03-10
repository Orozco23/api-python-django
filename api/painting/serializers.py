from rest_framework import serializers
from .models import Painting

class PaintingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = ['id', 'title', 'author', 'month_created', 'year_created', 'description', 'material', 'dimensions', 'creation_date', 'updated_date']
