from django.db import models


class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    biography = models.TextField()
    is_on_vacation = models.BooleanField(default=False)


class Department(models.Model):
    name = models.TextField()
    description = models.TextField()
    doctor = models.ForeignKey(
        Doctor, related_name="departments", on_delete=models.CASCADE
    )


class DoctorAvailabilty(models.Model):
    date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    doctor = models.ForeignKey(
        Doctor, related_name="availabilities", on_delete=models.CASCADE
    )


class MedicalNote(models.Model):
    doctor = models.ForeignKey(
        Doctor, related_name="medical_notes", on_delete=models.CASCADE
    )
    note = models.TextField()
    date = models.DateField()
