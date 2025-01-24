from rest_framework import serializers
from .models import TableName, DeviceTracking

class TableNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableName
        fields = ['id', 'question', 'answer', 'created_at']  # Specify fields to include in the API

class DeviceTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceTracking
        fields = ['id', 'ip_address', 'mac_address', 'created_at']