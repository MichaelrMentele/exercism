def to_rna(dna):
    transcriptions = {
        'A': 'U',
        'T': 'A',
        'C': 'G',
        'G': 'C',
    }

    transcription = ""
    for nucleotide in dna:
        valid = transcriptions.get(nucleotide, False)
        if valid:
            transcription += valid
        else:
            return ""
    return transcription
