from django.urls import path

from rest_framework.routers import DefaultRouter
from .viewsets import PatientViewSet, InsuranceViewSet, MedicalRecordViewSet

router = DefaultRouter()
router.register('patients', PatientViewSet, basename='patient')
router.register('insurances', InsuranceViewSet, basename='insurance')
router.register('medical-records', MedicalRecordViewSet, basename='medical-record')

urlpatterns = router.urls
