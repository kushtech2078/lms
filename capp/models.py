from django.db import models
from ckeditor.fields import RichTextField

class TableName(models.Model):
    question = models.CharField(max_length=255, null=False, blank=False)
    answer = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question