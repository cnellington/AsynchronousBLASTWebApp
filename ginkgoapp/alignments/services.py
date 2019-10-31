def get_alignment(sequence):
    from .models import Protein
    results = None
    if sequence:
        results = Protein.objects.filter(sequence__icontains=sequence)
    return results


def process_alignment(alignment):
    results = get_alignment(alignment.sequence)
    if results:
        prot = results[0]
        alignment.result_name = prot.description
        alignment.result_start = prot.sequence.lower().find(alignment.sequence.lower())
    else:
        alignment.result_name = "No Match"
        alignment.result_start = -1
    alignment.status = "Processed"
    alignment.save()