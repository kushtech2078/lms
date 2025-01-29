from django.contrib import admin
from .models import Type, Question
from ckeditor.widgets import CKEditorWidget
from django import forms

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'answer': CKEditorWidget(),  # Use CKEditor widget for the 'answer' field
        }

class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm

admin.site.register(Question, QuestionAdmin)
admin.site.register(Type)