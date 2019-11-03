from django.db import models
from django_q.tasks import async_task
from django.core.validators import FileExtensionValidator

status_choices = (("New", "New"), ("Processed", "Processed"))
upload_dir = "alignments/static/files/"


# Queryable protein
class Protein(models.Model):
    file = models.FileField(upload_to=f"{upload_dir}protein_files/",
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
    sequence = models.TextField()
    result_name = models.CharField(max_length=16, default="No Match")
    result_start = models.IntegerField(default=-1)
    status = models.CharField(choices=status_choices, default=status_choices[0][0], max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.status != 'Processed':
            async_task('alignments.services.process_alignment', self)

    def __str__(self):
        return f"{self.result_name}, {self.modified}"
