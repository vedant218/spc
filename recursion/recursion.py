def remove_left_recursion(productions, non_terminal):
    # Initialize the new productions list
    new_productions = []

    # Get all the productions for the non-terminal
    non_terminal_productions = [p for p in productions if p[0] == non_terminal]

    # Get all the productions that don't start with the non-terminal
    other_productions = [p for p in productions if p[0] != non_terminal]

    # Check if there is any left recursion for the non-terminal
    has_left_recursion = False
    for production in non_terminal_productions:
        if production[2][0] == non_terminal:
            has_left_recursion = True
            break

    if not has_left_recursion:
        # If there is no left recursion, return the original productions list
        return productions

    # Otherwise, remove the left recursion
    new_non_terminal = non_terminal + "'"
    for production in non_terminal_productions:
        if production[2][0] == non_terminal:
            # Replace the left recursive production
            new_production = (new_non_terminal,
                              production[2][1:] + (new_non_terminal,))
        else:
            # Add the non-left recursive production
            new_production = (
                non_terminal, production[2] + (new_non_terminal,))
        new_productions.append(new_production)

    # Add the epsilon production
    new_productions.append((new_non_terminal, ('epsilon',)))

    # Add the new productions to the other productions list
    for production in other_productions:
        new_productions.append((production[0], production[1] + (
            new_non_terminal,) if production[0] == non_terminal else production[1]))

    # Recursively remove left recursion for the new non-terminal
    new_productions = remove_left_recursion(new_productions, new_non_terminal)

    return new_productions


# Get the grammar from user input
grammar = input("Enter the grammar: ")

# Split the grammar into productions
productions = [tuple(p.strip().split(' ')) for p in grammar.split(';')]

# Get the starting non-terminal from user input
starting_non_terminal = input("Enter the starting non-terminal: ")

# Remove left recursion for the starting non-terminal
productions = remove_left_recursion(productions, starting_non_terminal)

# Print the new productions
print("New productions:")
for production in productions:
    print(" ".join(production), end="; ")
