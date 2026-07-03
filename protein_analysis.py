from dictionaries import codontab, aa_weights
from DNA_validation import validation
def protein_analysis (seq):
    sequence, error =  validation(seq)
    if error:
        return error
    if len(sequence) == 0:
        return "sequence is empty"
    result = ""
    length = len(sequence)
    start = None
    stop = None
    if length>=3:
        for i in range(0, len(sequence)-2):
            if sequence[i] == 'A'and sequence[i+1]== 'T' and sequence[i+2]== 'G':
                start = i
                result += f"The sequence contains a START codon at position {i}-{i+1}-{i+2}\n"
                break
        if start is not None:
            for i in range(start, len(sequence), 3):
                codon = ''.join(sequence[i:i + 3])
                if codon == 'TAA' or codon == 'TGA' or codon == 'TAG':
                    result += f"The sequence contains a STOP codon at position {i}-{i+1}-{i+2}\n"
                    stop = i
                    break
            if stop is not None and (stop-start)%3==0:
                amino_acids = ""
                for i in range(start, stop, 3):
                    codon = ''.join(sequence[i:i + 3])
                    amino_acids += codontab[codon]
                result += f"Amino acid content: {len(amino_acids)}\n"
                result += f"Amino acid sequence: {amino_acids}\n"
                weight = 0
                for i in amino_acids:
                    weight += aa_weights[i]
                result += f"Sequence weight: {weight}\n"
            else:
                result += "The sequence does not encode a protein.\n"
        else:
            result += "The sequence does not encode a protein.\n"
    else:
        result += "The sequence does not encode a protein.\n"


    return result

