from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'  # Or specify fields
        widgets = {
            'answer': CKEditorWidget(),  # Use CKEditor for rich text
        }

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField()