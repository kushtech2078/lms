from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import TableName, DeviceTracking
from .serializers import TableNameSerializer, DeviceTrackingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import get_client_ip  # Assuming the get_client_ip function is in utils.py
from django.http import JsonResponse

def qa_view(request):
    # Fetch all Q&A entries from the database
    qa_list = TableName.objects.all()
    return render(request, 'capp/index.html', {'qa_list': qa_list})

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

def track_device(request):
    ip_address = get_client_ip(request)  # Get the client's IP address
    mac_address = request.GET.get('mac_address')  # Assuming MAC address is passed in the URL
    device = DeviceTracking.objects.create(ip_address=ip_address, mac_address=mac_address)
    return JsonResponse({'message': 'Device tracked successfully', 'ip_address': ip_address})

class DeviceTrackingAPIView(APIView):
    def post(self, request):
        # Get the client IP and MAC address from request
        ip_address = get_client_ip(request)
        mac_address = request.META.get('HTTP_X_MAC_ADDRESS', None)  # Retrieve from the header

        # Save the information in the database
        DeviceTracking.objects.create(
            ip_address=ip_address,
            mac_address=mac_address
        )

        return Response({"status": "saved"}, status=200)
    
class DeviceTrackingView(APIView):
    def post(self, request):
        ip_address = get_client_ip(request)  # Get the client's IP address
        mac_address = request.data.get('mac_address')  # Assuming MAC address is sent in POST data

        # Create and save the device info
        device = DeviceTracking.objects.create(ip_address=ip_address, mac_address=mac_address)
        return Response({'message': 'Device tracked successfully', 'ip_address': ip_address}, status=status.HTTP_201_CREATED)
