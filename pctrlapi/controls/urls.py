from django.urls import path
from .views import ControlListCreateAPIView, ControlDetailAPIView, ControlExportListImportCreateAPIView

urlpatterns = [
    path('', ControlListCreateAPIView.as_view(), name="list"),
    path('<int:pk>/', ControlDetailAPIView.as_view(), name="detail"),
    path('csv/',  ControlExportListImportCreateAPIView.as_view(), name="listcsv"),
]
