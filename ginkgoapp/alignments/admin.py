from django.contrib import admin
from alignments.models import Protein, Alignment

class ProteinAdmin(admin.ModelAdmin):
    fields = ['file',]

admin.site.register(Protein, ProteinAdmin)
admin.site.register(Alignment)
