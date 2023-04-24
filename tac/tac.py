# Define a dictionary to store the TAC
tac = {}

# Define a counter to keep track of the next available temporary variable
temp_counter = 0

# Function to generate a new temporary variable


def new_temp():
    global temp_counter
    temp_counter += 1
    return f"t{temp_counter}"

# Function to generate TAC for an arithmetic expression


def gen_tac(expr):
    # Split the expression into tokens
    tokens = expr.split()

    # Initialize the result variable to the first operand
    result = tokens[0]

    # Loop over the rest of the tokens
    for i in range(1, len(tokens), 2):
        # Generate a new temporary variable
        temp = new_temp()

        # Generate TAC for the current operation
        op = tokens[i]
        arg1 = result
        arg2 = tokens[i+1]
        tac[temp] = (op, arg1, arg2)

        # Update the result variable
        result = temp

    # Return the final temporary variable
    return result


# Example usage
expr = "a + b * c - d"
result = gen_tac(expr)
print(tac)
