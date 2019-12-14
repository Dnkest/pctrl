
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Control
from .serializers import ControlSerializer

class ControlListAPIView(ListCreateAPIView):
    queryset = Control.objects.all()
    serializer_class = ControlSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'created_by', 'type', 'maximum_rabi_rate', 'polar_angle']

class ControlDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Control.objects.all()
    serializer_class = ControlSerializer
