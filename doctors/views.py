from django.shortcuts import render
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class ListDoctorsViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]
    
class DetailDoctorView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer