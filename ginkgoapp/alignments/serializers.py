from rest_framework import serializers
from alignments.models import Alignment

# Alignment Serializer
class AlignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alignment
        fields = ('id', 'sequence', 'result_name', 'result_start', 'status')
