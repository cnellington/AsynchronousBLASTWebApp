from rest_framework import serializers
from alignments.models import Alignment

# Alignment Serializer
class AlignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alignment
        fields = '__all__'
