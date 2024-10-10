from rest_framework import serializers

from .models import Doctor, Department, DoctorAvailabilty, MedicalNote

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DoctorAvailabiltySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailabilty
        fields = '__all__'
        
class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = '__all__'