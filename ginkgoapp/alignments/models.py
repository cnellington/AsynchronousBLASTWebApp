from django.db import models
from django_q.tasks import async_task

from . import services


# Queryable protein
class Protein(models.Model):
    reference = models.CharField(max_length=16)
    description = models.CharField(max_length=128)
    sequence = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


# Search result
class Alignment(models.Model):
    # user = ??  TODO: store IP address or session
    sequence = models.TextField()
    result_name = models.CharField(max_length=16, default="No Match")
    result_start = models.IntegerField(default=-1)
    status = models.CharField(choices=(("Processed", "Processed"), ("New", "New")), default="New", max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.status != 'Processed':
            async_task('alignments.services.process_alignment', self)
        super().save(*args, **kwargs)
