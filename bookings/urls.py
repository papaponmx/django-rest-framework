from rest_framework.routers import DefaultRouter

from .viewsets import AppointmentViewSet, MedicalNoteViewSet

router = DefaultRouter()
router.register('appointments', AppointmentViewSet, basename='appointment')
router.register('medical-notes', MedicalNoteViewSet, basename='medical-note')

urlpatterns = router.urls
