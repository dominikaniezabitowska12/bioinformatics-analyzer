from DNA_validation import validation
def mutation_analysis(reference_sequence, analyzed_sequence):
    reference_sequence, error = validation(reference_sequence)
    if error:
        return error
    analyzed_sequence, error = validation(analyzed_sequence)
    if error:
        return error
    result = ''
    if len(reference_sequence) > len(analyzed_sequence):
        result += "Mutations detected: deletion"
    elif len(analyzed_sequence) > len(reference_sequence):
        result += "Mutation detected: insertion"
    elif reference_sequence == analyzed_sequence:
        result += "No mutation"
    else:
        result += "Mutations detected: substitution\n"
        for i in range(len(reference_sequence)):
            if reference_sequence[i] != analyzed_sequence[i]:
                result += f"Mutation position: {i+1} nucleotide. {reference_sequence[i]} -> {analyzed_sequence[i]}\n"

    return result