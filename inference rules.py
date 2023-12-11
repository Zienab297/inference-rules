# Define the six inference rules as functions

def modus_ponens(premises):
    for i in range(len(premises)):
        for j in range(i+1, len(premises)):
            p = premises[i]
            q = premises[j]

            if p[0] == q[0] and p [1] == '->' and q[1] == ' ' and q [2] == ' ':
                return p[-1]
    return None


def modus_tollens(premises):
    for i in range(len(premises)):
        for j in range(i+1, len(premises)):
            p = premises[i]
            q = premises[j]
            if p[1] == '->' and len(q) == 2 and q[0] == '~' and q[1] == p[-1]:
                return ['~' + p[0]]
            return None

def hypothetical_syllogism(premises):
    for i in range(len(premises)):
        for j in range(i+1, len(premises)):
            p = premises[i]
            q = premises[j]
            if p[1] == '->' and q[1] == '->' and p[2] == q[0]:
                return (p[0], '->', q[2])
    return None

def disjunctive_syllogism(premises):
    for i in range(len(premises)):
        for j in range(i+1, len(premises)):
            p = premises[i]
            q = premises[j]

            if p[1] == 'v' and q[0] == '~' and p[2] == q[1]:
                return (p[0])
            elif p[1] == 'v' and q[0] == '~' and p[0] == q[1]:
                return (p[-1])
    return None

def addition(premises):
    for i in range(len(premises)):
        for j in range(i+1, len(premises)):
            p = premises[i]
            q = premises[j]

            if p[1] == q[0]:
                return (p[0], 'v', 'q')
    return None

def simplification(premises):
    for p in premises:
        if p[1] == '^':
            return (p[0],), (p[2],)
    return None


# Example premises remove the \# to run
#premises = [ ('p', '->', 'q'),('q', '->', 'r')]
#premises = [ ('p', '->', 'q'),('p', ' ', ' ')]
#premises = [ ('p', '->', 'q'),('~', 'q')]
#premises = [ ('p', 'v', 'q'),('~', 'p')]
#premises = [ ('p', ' ', ' '),(' ', ' ', ' ')]
#premises = [ ('p', '^', 'q'),(' ', ' ', ' ')]

# Apply each inference rule to the premises until a valid conclusion is found
inference_rules = [modus_ponens, modus_tollens, hypothetical_syllogism, disjunctive_syllogism, addition, simplification]
for rule in inference_rules:
    conclusion = rule(premises)
    if conclusion is not None and conclusion not in premises:
        print(f"Valid conclusion: {conclusion}")
        break