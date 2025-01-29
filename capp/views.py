# views.py
from django.shortcuts import render, redirect
from .models import Type, Question
from django.http import HttpResponse
import pandas as pd
from .forms import ExcelUploadForm

def question_list(request):
    # Get all types
    types = Type.objects.all()
    
    # Get questions grouped by type
    questions_by_type = {}
    for type_obj in types:
        questions_by_type[type_obj] = Question.objects.filter(type=type_obj)
    
    return render(request, 'capp/index.html', {'questions_by_type': questions_by_type, 'types': types})

def handle_uploaded_file(file):
    # Read the Excel file
    df = pd.read_excel(file)

    # Iterate over the rows of the dataframe and save data
    for index, row in df.iterrows():
        type_name = row["Type"].strip()  # Get type name from the row
        question_text = row["Question"].strip()  # Get question text
        answer_text = row["Answer"].strip()  # Get answer text

        # Get or create the Type instance based on the type name
        question_type, _ = Type.objects.get_or_create(name=type_name)

        # Create a Question instance and save it
        Question.objects.create(type=question_type, question=question_text, answer=answer_text)

# View to handle the Excel file upload
def upload_excel(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']
        try:
            # Call the function to process the uploaded file
            handle_uploaded_file(excel_file)
            return HttpResponse("Excel file imported successfully.")
        except Exception as e:
            return HttpResponse(f"Error: {e}")

    form = ExcelUploadForm()
    return render(request, 'capp/upload_excel.html', {'form': form})