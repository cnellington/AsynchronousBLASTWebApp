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
    alignment = models.ForeignKey(Protein, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
