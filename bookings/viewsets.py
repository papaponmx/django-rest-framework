from rest_framework import viewsets

from .serializers import AppointmentSerializer, MedicalNoteSerializer
from .models import Appointment, MedicalNote

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    
class MedicalNoteViewSet(viewsets.ModelViewSet):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer


