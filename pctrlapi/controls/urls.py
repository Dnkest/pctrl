from django.urls import path
from .views import ControlListAPIView, ControlDetailAPIView

urlpatterns = [
    path('', ControlListAPIView.as_view(), name="list"),
    path('<int:pk>/', ControlDetailAPIView.as_view(), name="detail"),
]
