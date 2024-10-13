from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import DoctorSerializer, DepartmentSerializer, DoctorAvailabiltySerializer, MedicalNoteSerializer
from .models import Doctor, Department, DoctorAvailabilty, MedicalNote

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    
    @action(["POST"], detail=True, url_path="set-on-vacation")
    def set_on_vacation(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        return Response({"is_on_vacation": doctor.is_on_vacation})

    @action(["POST"], detail=True, url_path="set-off-vacation")
    def set_off_vacation(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({"is_on_vacation": doctor.is_on_vacation})

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = DoctorAvailabilty.objects.all()
    serializer_class = DoctorAvailabiltySerializer  

class MedicalNoteViewSet(viewsets.ModelViewSet):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer
