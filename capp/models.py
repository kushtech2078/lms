from django.db import models
from ckeditor.fields import RichTextField

class TableName(models.Model):
    question = models.CharField(max_length=255, null=False, blank=False)
    answer = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
    
class DeviceTracking(models.Model):
    ip_address = models.GenericIPAddressField()
    mac_address = models.CharField(max_length=17, null=True, blank=True)  # MAC address is 17 characters long
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"IP: {self.ip_address} - MAC: {self.mac_address} - Time: {self.created_at}"