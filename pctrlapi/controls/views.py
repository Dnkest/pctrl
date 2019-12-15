from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_csv.parsers import CSVParser
from rest_framework_csv.renderers import CSVStreamingRenderer
from rest_framework_files.generics import ExportListImportCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Control
from .serializers import ControlSerializer, ControlCSVSerializer

class ControlListAPIView(ListCreateAPIView):
    queryset = Control.objects.all()
    serializer_class = ControlSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'type', 'maximum_rabi_rate', 'polar_angle']

class ControlDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Control.objects.all()
    serializer_class = ControlSerializer

class ControlListCSVAPIView(ExportListImportCreateAPIView):
    queryset = Control.objects.all()
    serializer_class = ControlCSVSerializer
    paginator = None
    filename = 'controls'

    # renderer classes used to render the content. will determine the file type of the download
    renderer_classes = (CSVStreamingRenderer, )
    parser_classes = (MultiPartParser, FormParser)

    # parser classes used to parse the content of the uploaded file
    file_content_parser_classes = (CSVParser, )
