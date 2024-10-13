from django.urls import path

from doctors.views import ListDoctorsViewSet, DetailDoctorView 

from rest_framework.routers import DefaultRouter
from .viewsets import DoctorViewSet, DepartmentViewSet, DoctorAvailabilityViewSet, MedicalNoteViewSet

router = DefaultRouter()
router.register('doctors', DoctorViewSet, basename='doctor')
router.register('departments', DepartmentViewSet, basename='department')
router.register('doctor-availabilities', DoctorAvailabilityViewSet, basename='doctor-availability')
router.register('medical-notes', MedicalNoteViewSet, basename='medical-note')

urlpatterns = router.urls
