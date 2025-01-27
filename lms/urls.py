"""
URL configuration for lms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from capp import views
from capp.views import qa_view
from django.urls import path
from capp.views import TableNameListCreateAPIView, TableNameRetrieveUpdateDestroyAPIView, TableNameSearchAPIView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.qa_view, name='qa_view'),
    path('upload_excel/', views.upload_excel, name='upload_excel'),
    path('download_excel/', views.download_excel, name='download_excel'),
    path('table_name_list/', views.table_name_list, name='table_name_list'),  # Add this line
    path('api/tablename/', TableNameListCreateAPIView.as_view(), name='tablename-list-create'),  # List and Create
    path('api/tablename/<int:pk>/', TableNameRetrieveUpdateDestroyAPIView.as_view(), name='tablename-detail'),  # Retrieve, Update, Delete
    path('api/tablename/search/', TableNameSearchAPIView.as_view(), name='tablename-search'),
]
