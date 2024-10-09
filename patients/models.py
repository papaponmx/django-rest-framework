from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    medical_history = models.TextField()


class Insurance(models.Model):
    provider = models.TextField()
    policy_number = models.TextField()
    expiration_date = models.DateField()
    patient = models.ForeignKey(
        Patient, related_name="insurances", on_delete=models.CASCADE
    )


class MedicalRecord(models.Model):
    date = models.DateField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    follow_up_date = models.DateField()
    patient = models.ForeignKey(
        Patient, related_name="medical_records", on_delete=models.CASCADE
    )
