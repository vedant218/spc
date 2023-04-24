def compute_first(grammar):
    first = {}
    for nt in grammar:
        first[nt] = {}
    for nt in grammar:
        for rule in grammar[nt]:
            if len(rule) > 0 and rule[0] not in grammar:
                first[nt][rule[0]] = True
            elif len(rule) > 0 and rule[0] in grammar:
                for term, _ in compute_first(grammar, rule[0]).items():
                    first[nt][term] = True
    return first


grammar = {
    'S': [['a', 'B'], ['b', 'S'], ['c']],
    'B': [['d'], ['e']]
}

first_sets = compute_first(grammar)
print(first_sets)
