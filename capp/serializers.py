from rest_framework import serializers
from .models import TableName

class TableNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableName
        fields = ['id', 'question', 'answer', 'created_at']  # Specify fields to include in the API
