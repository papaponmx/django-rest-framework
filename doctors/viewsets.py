from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from bookings.serializers import AppointmentSerializer
from bookings.models import Appointment
from .serializers import DoctorSerializer, DepartmentSerializer, DoctorAvailabiltySerializer, MedicalNoteSerializer
from .models import Doctor, Department, DoctorAvailabilty, MedicalNote
from .permissions import IsDoctor

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsDoctor]
    
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
    
    @action(['POST', 'GET'], detail=True, serializer_class=AppointmentSerializer)
    def appointments(self,  request, pk=None):
        doctor =  self.get_object()
        
        if request.method  == 'POST':
            data = request.data.copy()
            data['doctor'] = doctor.id            
            serializer = AppointmentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_201_CREATED)
        
        if request.method == 'GET':
            appointments = Appointment.objects.filter(doctor=doctor)
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data)
    
    @action(['GET', 'DELETE'], detail=True, url_path='appointments/(?P<appointment_id>[0-9]+)')
    def appointment(self, request, pk=None, appointment_id=None):
        
        if request.method == 'GET':
            appointments = Appointment.objects.get(id=appointment_id)
            serializer = AppointmentSerializer(appointments)
            return Response(serializer.data)
        if request.method == 'DELETE':
            doctor = self.get_object()
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = DoctorAvailabilty.objects.all()
    serializer_class = DoctorAvailabiltySerializer  

class MedicalNoteViewSet(viewsets.ModelViewSet):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer
