from rest_framework import viewsets

from .serializers import DoctorSerializer, DepartmentSerializer, DoctorAvailabiltySerializer, MedicalNoteSerializer
from .models import Doctor, Department, DoctorAvailabilty, MedicalNote

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = DoctorAvailabilty.objects.all()
    serializer_class = DoctorAvailabiltySerializer  

class MedicalNoteViewSet(viewsets.ModelViewSet):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer
