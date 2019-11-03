import json
from alignments.models import Alignment
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import AlignmentSerializer

# Alignment Viewset
class AlignmentViewSet(viewsets.ModelViewSet):
    queryset = Alignment.objects.all().filter(status='Processed').order_by('-modified')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AlignmentSerializer

    @action(detail=False, methods=['post'], url_path='id-specific', url_name='id_specific')
    def get_alignments_by_id(self, request):
        ids = json.loads(request.data['ids'])
        user_queries = self.queryset.filter(id__in=ids)
        return Response([AlignmentSerializer(query).data for query in user_queries])