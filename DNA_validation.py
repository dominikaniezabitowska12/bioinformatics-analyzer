def validation(seq):
    seq = seq.upper()
    sequence = []
    for i in seq:
        if i not in "ATCG":
            return None, f'{i} is an incorrect nucleotide\n'
        else:
            sequence.append(i)

    return sequence, None

















