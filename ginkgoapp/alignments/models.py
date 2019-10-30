from django.db import models

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
    result_name = models.CharField(max_length=16, blank=True)
    result_start = models.IntegerField(blank=True)
    status = models.CharField(choices=(("Processed", "Processed"), ("New", "New")), default="New", max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # TODO: Run async alignment on proteins, mark processed
        results = services.get_alignment(self.sequence)
        if results:
            prot = results[0]
            self.result_name = prot.description
            self.result_start = prot.sequence.lower().find(self.sequence.lower())
        else:
            self.result_name = "No Match"
            self.result_start = -1
        self.status = "Processed"
        super().save(*args, **kwargs)
