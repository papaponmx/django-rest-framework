from .serializers import PatientSerializer
from .models import Patient
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class ListPatientsView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DetailPatientView(RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer