from django.urls import path

from doctors.views import ListDoctorsViewSet, DetailDoctorView 

urlpatterns = [
    path('doctors', ListDoctorsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('doctors/<int:pk>/', DetailDoctorView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
