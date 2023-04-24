# function to calculate FIRST set of a given non-terminal
def first(input_grammar, non_terminal, visited):
    # if the non-terminal has already been visited, return the previously calculated FIRST set
    if non_terminal in visited:
        return visited[non_terminal]

    # initialize the FIRST set for the non-terminal
    first_set = set()

    # iterate over each production rule in the grammar
    for production in input_grammar[non_terminal]:
        # if the production starts with a terminal symbol, add it to the FIRST set
        if production[0] not in input_grammar.keys():
            first_set.add(production[0])
        # if the production starts with a non-terminal symbol, recursively calculate its FIRST set
        else:
            # iterate over the symbols in the production
            for symbol in production:
                # calculate the FIRST set of the non-terminal symbol
                first_of_symbol = first(input_grammar, symbol, visited)
                # add the FIRST set to the FIRST set of the non-terminal
                first_set = first_set.union(first_of_symbol)
                # if the symbol does not derive epsilon, stop iterating
                if 'epsilon' not in first_of_symbol:
                    break

    # store the calculated FIRST set in the visited dictionary
    visited[non_terminal] = first_set

    return first_set


input_grammar = {
    'S': [['A'], ['C', 'd']],
    'A': [['a'], ['$']],
    'B': [['b'], ['$']],
    'C': [['c']]
}

# initialize the visited dictionary
visited = {}

# calculate the FIRST set of the non-terminal 'S'
first_S = first(input_grammar, 'S', visited)

# print the calculated FIRST set
print('FIRST(S) =', first_S)
