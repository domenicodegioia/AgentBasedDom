from csp.ac3 import AC3
from csp.backtracking import *
from csp.contraints import Constraint
from csp.problem import CSP


# VARIABLES
trash = ["t1", "t2", "t3", "t4", "t5"]
food = ["f1", "f2", "f3"]
explosive = ["e1", "e2"]
frozen = ["fz1", "fz2", "fz3"]
fresh = ["fs1"]
variables = [x for x in trash + food + explosive + frozen + fresh]


# DOMAINS
# Number of containers = 4
# Maximum capacity for a container = 6
domains = {}
map_containers = [("Container " + str(i), j) for i in range(1, 5) for j in range(1, 7)]
for variable in variables:
    domains[variable] = map_containers.copy()


# CONSTRAINTS

class SplitItemsConstraint(Constraint):
    def __init__(self, v1, v2):
        super().__init__(variables=[v1, v2])
        self.v1 = v1
        self.v2 = v2

    def check(self, state):
        if self.v1 not in state or self.v2 not in state:
            return True
        return state[self.v1][0] != state[self.v2][0]


class TogetherItemsConstraint(Constraint):
    def __init__(self, v1, v2):
        super().__init__(variables=[v1, v2])
        self.v1 = v1
        self.v2 = v2

    def check(self, state):
        if self.v1 not in state or self.v2 not in state:
            return True
        return state[self.v1][0] == state[self.v2][0]


class AllDiffConstraint(Constraint):
    def __init__(self, v1):
        super().__init__(variables=[v1])
        self.v1 = v1

    def check(self, state):
        for x in state:
            if x != self.v1 and state[x] == state[self.v1]:
                return False
        return True

constraints = []

# all the Explosive items must be put in different containers
for e1 in explosive:
    for e2 in explosive:
        if e1 != e2:
            constraints.append(SplitItemsConstraint(e1, e2))

# Trash items cannot be in the same container with a Food item
for f in food:
    for t in trash:
        constraints.append(SplitItemsConstraint(f, t))
        constraints.append(SplitItemsConstraint(t, f))

# Frozen items must be all within the same container
for fz1 in frozen:
    for fz2 in frozen:
        if fz1 != fz2:
            constraints.append(SplitItemsConstraint(fz1, fz2))

# Fresh and Frozen items cannot be within the same container
for fs in fresh:
    for fz in frozen:
        constraints.append(SplitItemsConstraint(fs, fz))
        constraints.append(SplitItemsConstraint(fz, fs))

for v in variables:
        constraints.append(AllDiffConstraint(v))

# CSP
problem = CSP(variables=variables, domains=domains, constraints=constraints)
initial_state = {}


print('Pre-processing w/ AC3')
print(f'Domains before the pre-processing step: \n{problem.domains}')
optimizer = AC3(csp=problem)
optimizer.run(state=initial_state)
print(f'\ndomains after the pre-processing step: \n{problem.domains}')


search = BackTracking(problem=problem,
                      var_criterion=degree_heuristic,
                      value_criterion=least_constraining_value)
print('\n\nApply search using Backtracking algorithm')
solution = search.run(state=initial_state)

if not solution:
    print("No solution found")
else:
    print('\nSolution:')
    for var in solution:
        print('\t', var, '\t:', solution[var])