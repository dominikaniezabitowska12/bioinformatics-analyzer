from DNA_validation import validation

def sequence_analysis(seq):
    sequence, error  = validation(seq)
    if error:
        return error
    if len(sequence) == 0:
        return "sequence is empty"
    result = ''
    length = len(sequence)
    result += f'Sequence length: {length} nucleotides\n'

    amount_of_A = sequence.count('A')
    amount_of_C = sequence.count('C')
    amount_of_G = sequence.count('G')
    amount_of_T = sequence.count('T')
    result += (f'Adenine content: {amount_of_A/length*100:.2f}%\n'
                f'Cytosine content: {amount_of_C/length*100:.2f}%\n'
                f'Guanine content: {amount_of_G/length*100:.2f}%\n'
                f'Thymine content: {amount_of_T/length*100:.2f}%\n')


    GC_count = amount_of_C + amount_of_G
    GCcontent = GC_count/length*100
    result += f'GC content: {GCcontent:.2f}%\n'

    protein = 0
    if length >= 3:
        if sequence[0] == 'A' and sequence[1] == 'T' and sequence[2] == 'G':
            result += 'START codon: YES\n'
            protein += 1
        else:
            result += 'START codon: NO\n'

    if length >= 3:
        if sequence[-3] == 'T' and sequence[-2] == 'A' and sequence[-1] == 'A':
            result += 'STOP codon: YES\n'
            protein += 1
        elif sequence[-3] == 'T' and sequence[-2] == 'A' and sequence[-1] == 'G':
            result += 'STOP codon: YES\n'
            protein += 1
        elif sequence[-3] == 'T' and sequence[-2] == 'G' and sequence[-1] == 'A':
            result += 'STOP codon: YES\n'
            protein += 1
        else:
            result +='STOP codone: NO\n'


    if length % 3 == 0:
        protein += 1


    if protein == 3:
        result +="The sequence encodes a protein.\n"
    else:
        result +="The sequence does not encode a protein.\n"

    return result


