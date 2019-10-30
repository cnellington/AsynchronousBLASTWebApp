from django.core.management.base import BaseCommand, CommandError

from Bio import SeqIO

from alignments.models import Protein

class Command(BaseCommand):
    help = 'Populate Proteins from .fasta files'

    def handle(self, *args, **options):
        targets = ["NC_000852", "NC_007346", "NC_008724", "NC_009899", "NC_014637", "NC_020104", "NC_023423",
                   "NC_023640", "NC_023719", "NC_027867"]

        for target in targets:
            with open(f"../files/{target}.fasta", "rU") as handle:
                for record in SeqIO.parse(handle, "fasta"):
                    print(record.id)
                    print(record.description)
                    print(record.seq[0:10])
                    print()
                    Protein.objects.get_or_create(reference=target, description=record.description, sequence=record.seq)