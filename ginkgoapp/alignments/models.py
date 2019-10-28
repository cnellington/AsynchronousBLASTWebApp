from django.db import models


# Queryable protein
class Protein(models.Model):
    ref = models.CharField(max_length=10)
    name = models.CharField(max_length=128)
    sequence = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


# Search result
class Alignment(models.Model):
    # user = ??  TODO: store IP address or session
    sequence = models.TextField()
    status = models.CharField(choices=(("Processed", "Processed"), ("New", "New")), default="New", max_length=10)
    alignment = models.ForeignKey(Protein, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # TODO: Run async alignment on proteins, mark processed
        self.alignment = Protein.objects.all()[0] # placeholder
        super().save(*args, **kwargs)
