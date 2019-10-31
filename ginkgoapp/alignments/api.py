from alignments.models import Alignment
from rest_framework import viewsets, permissions
from .serializers import AlignmentSerializer

# Alignment Viewset
class AlignmentViewSet(viewsets.ModelViewSet):
    queryset = Alignment.objects.all().filter(status='Processed').order_by('-modified')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AlignmentSerializer
