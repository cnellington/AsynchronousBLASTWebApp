def get_alignment(sequence):
    from .models import Protein
    results = None
    if sequence:
        results = Protein.objects.filter(sequence__icontains=sequence)
    return results