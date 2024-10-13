from django.shortcuts import render
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework import viewsets

class ListDoctorsViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    
class DetailDoctorView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer