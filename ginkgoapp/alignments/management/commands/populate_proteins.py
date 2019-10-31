from django.core.management.base import BaseCommand, CommandError

from Bio import SeqIO

from alignments.models import Protein, status_choices

class Command(BaseCommand):
    help = 'Populate Proteins uploaded .fasta files'

    def handle(self, *args, **options):

        for protein in Protein.objects.filter(status=status_choices[0][0]):
            try:
                with protein.file.open('rU') as handle:
                    for record in SeqIO.parse(handle, "fasta"):
                        protein.name = record.id,
                        protein.description = record.description,
                        protein.sequence = record.seq
                        protein.status = status_choices[1][0]
                        protein.save()
            except FileNotFoundError:
                print(f"File for Protein {protein.id} not found")