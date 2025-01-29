from django.db import models
from ckeditor.fields import RichTextField

# Define the Type model (as done above)
class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Define the Question model with a ForeignKey to the Type model
class Question(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)  # ForeignKey field
    question = models.TextField()  # The question itself
    answer = RichTextField()  # The answer to the question

    def __str__(self):
        return f"Question: {self.question}"