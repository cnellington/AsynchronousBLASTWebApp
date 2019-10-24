from rest_framework import routers
from .api import AlignmentViewSet

router = routers.DefaultRouter()
router.register('api/alignments', AlignmentViewSet, 'alignments')

urlpatterns = router.urls
