from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_csv.parsers import CSVParser
from rest_framework_csv.renderers import CSVStreamingRenderer
from rest_framework_files.generics import ExportListImportCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Control
from .serializers import ControlSerializer, ControlCSVSerializer

class ControlListCreateAPIView(ListCreateAPIView):
    """
    List all controls [GET].
    Create a new control [POST].
    You can also filter the result with query parameters.
    """
    queryset = Control.objects.all()
    serializer_class = ControlSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'type', 'maximum_rabi_rate', 'polar_angle']

class ControlDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a specific control [GET].
    Update a specific control [PUT].
    Delete a specific control [DELETE].
    """
    queryset = Control.objects.all()
    serializer_class = ControlSerializer

class ControlExportListImportCreateAPIView(ExportListImportCreateAPIView):
    """
    Bulk upload controls in CSV format [POST].
    Download controls in CSV format [GET].
    """
    queryset = Control.objects.all()
    serializer_class = ControlCSVSerializer
    paginator = None    # dump all controls
    filename = 'controls'

    # renderer classes used to render the content. will determine the file type of the download
    renderer_classes = (CSVStreamingRenderer, )
    parser_classes = (MultiPartParser, FormParser)

    # parser classes used to parse the content of the uploaded file
    file_content_parser_classes = (CSVParser, )
