from rest_framework import serializers

from .models import Doctor, Department, DoctorAvailabilty, MedicalNote

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        
    def validate_email(self, value):
        if "@example.com"  in value or "@hey.com" in value:
            return value
        raise serializers.ValidationError("Email has to be example.com")
        
    def validate(self, attrs):
        if len(attrs['contact_number']) < 10 and attrs['is_on_vacation']:
            raise serializers.ValidationError(
                "Contact number cannot be more than 10 digits when on vacation"
            )
        return super().validate(attrs)
            
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