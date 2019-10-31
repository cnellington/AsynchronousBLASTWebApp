from django.db import models
from django_q.tasks import async_task
from django.core.validators import FileExtensionValidator


status_choices = (("New", "New"), ("Processed", "Processed"))


# Queryable protein
class Protein(models.Model):
    file = models.FileField(upload_to='static/files/protein_files',
                            validators=[FileExtensionValidator(allowed_extensions=['fasta'])])
    status = models.CharField(choices=status_choices, default=status_choices[0][0], max_length=10)
    name = models.CharField(max_length=16, blank=True, null=True)
    description = models.CharField(max_length=128, blank=True, null=True)
    sequence = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.description:
            return f"{self.description}"
        return "Unprocessed"


# Search result
class Alignment(models.Model):
    # user = ??  TODO: store IP address or session
    sequence = models.TextField()
    result_name = models.CharField(max_length=16, default="No Match")
    result_start = models.IntegerField(default=-1)
    status = models.CharField(choices=status_choices, default=status_choices[0][0], max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.status != 'Processed':
            async_task('alignments.services.process_alignment', self)
        super().save(*args, **kwargs)
