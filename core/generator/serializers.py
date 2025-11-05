from rest_framework import serializers
from .models import Quote, Author

class QuoteSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Quote
        fields = ['id', 'quote', 'author']
