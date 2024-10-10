from .serializers import PatientSerializer
from .models import Patient

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Since this does not take parameters we will use the same view
@api_view(["GET", "POST"])
def list_patients(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PatientSerializer(data=request.data)  # Deserializar los datos enviados por el cliente
        serializer.is_valid(raise_exception=True)
        serializer.save()  # Guardar el nuevo paciente en la base de datos
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # Devolver los datos del paciente creado

@api_view(["GET", "PUT", "DELETE"])
def detail_patient(request, pk):
    if request.method == 'GET':
        try: 
            patient = Patient.objects.get(id=pk)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSerializer(patient)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        try:
            patient = Patient.objects.get(id=pk)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    