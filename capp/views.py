from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import TableName
from .serializers import TableNameSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def function_name(request):
  return HttpResponse("abc")

# List and Create API
class TableNameListCreateAPIView(ListCreateAPIView):
    queryset = TableName.objects.all()
    serializer_class = TableNameSerializer

    # Add search and sorting capabilities
    filter_backends = [SearchFilter, OrderingFilter]

    # Specify fields for searching
    search_fields = ['question', 'answer']  # Fields to search in

    # Specify fields for ordering
    ordering_fields = ['created_at', 'question']  # Fields to sort by
    ordering = ['created_at']  # Default ordering

# Retrieve, Update, and Delete API
class TableNameRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TableName.objects.all()
    serializer_class = TableNameSerializer

class TableNameSearchAPIView(ListAPIView):
    queryset = TableName.objects.all()
    serializer_class = TableNameSerializer
    filter_backends = [SearchFilter]
    search_fields = ['question', 'answer']  # Allow searching in both 'question' and 'answer'


class TableNameSearchAPIView(APIView):
    def get(self, request):
      question_query = request.GET.get('question', None)  # Search for question
      answer_query = request.GET.get('answer', None)  # Search for answer
      
      if question_query:
        queryset = TableName.objects.filter(question__icontains=question_query)
      elif answer_query:
        queryset = TableName.objects.filter(answer__icontains=answer_query)
      else:
        queryset = TableName.objects.all()  # Return all if no search is applied

      serializer = TableNameSerializer(queryset, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)