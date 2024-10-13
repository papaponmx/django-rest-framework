from django.urls import path

from doctors.views import ListDoctorsViewSet, DetailDoctorView 

from rest_framework.routers import DefaultRouter
from .viewsets import DoctorViewSet

router = DefaultRouter()
router.register('doctors', DoctorViewSet, basename='doctor')

urlpatterns = [
    path('doctors', ListDoctorsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('doctors/<int:pk>/', DetailDoctorView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
] + router.urls
