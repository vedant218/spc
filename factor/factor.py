def left_factor(grammar):
    nonterminals = set()
    productions = {}
    for rule in grammar:
        nonterm, prod = rule.split(" -> ")
        nonterminals.add(nonterm)
        if nonterm not in productions:
            productions[nonterm] = []
        productions[nonterm].append(prod)

    new_productions = {}
    for nonterm in nonterminals:
        prods = productions[nonterm]
        while len(prods) > 1:
            prefix = os.path.commonprefix(prods)
            if len(prefix) > 0:
                factor = nonterm + "'"
                new_productions[factor] = [prefix]
                for i, prod in enumerate(prods):
                    if prod.startswith(prefix):
                        prods[i] = prod[len(prefix):]
                    else:
                        prods[i] = prod
                new_productions[nonterm] = [
                    factor + " " + prod for prod in prods]
                nonterm = factor
                prods = [new_productions[factor][0]] + prods[1:]
            else:
                break
        new_productions[nonterm] = prods

    new_grammar = []
    for nonterm in nonterminals:
        prods = new_productions[nonterm]
        for prod in prods:
            new_grammar.append(nonterm + " -> " + prod)

    return new_grammar


# Example usage
grammar = ["S -> AB | AC | AD",
           "A -> a | aB",
           "B -> b | bB | bC",
           "C -> c | cD",
           "D -> d"]
new_grammar = left_factor(grammar)
print(new_grammar)
