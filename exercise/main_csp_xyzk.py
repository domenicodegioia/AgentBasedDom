from csp.ac3 import AC3
from csp.backtracking import *
from csp.contraints import Constraint
from csp.problem import CSP

variables = ['X', 'Y', 'Z', 'K']
domains = {
    'X': [i for i in range(4, 11)],
    'Y': [i for i in range(2, 16)],
    'Z': [i for i in range(4, 36)],
    'K': [i for i in range(7, 29)]
}


class Cxy(Constraint):
    def check(self, state):
        if self.variables[0] in state and self.variables[1] in state:
            return state[self.variables[0]] <= state[self.variables[1]]
        else:
            return True


class Cyx(Constraint):
    def check(self, state):
        if self.variables[0] in state and self.variables[1] in state:
            return state[self.variables[0]] >= state[self.variables[1]]
        else:
            return True


class Cxz(Constraint):
    def check(self, state):
        if self.variables[0] in state and self.variables[1] in state:
            return state[self.variables[0]] < state[self.variables[1]]
        else:
            return True


class Czx(Constraint):
    def check(self, state):
        if self.variables[0] in state and self.variables[1] in state:
            return state[self.variables[0]] > state[self.variables[1]]
        else:
            return True


class Ckz(Constraint):
    def check(self, state):
        if self.variables[0] in state and self.variables[1] in state:
            return state[self.variables[0]] == state[self.variables[1]]
        else:
            return True


constraints = [Cxy(['X', 'Y']), Cyx(['Y', 'X']), Cxz(['X', 'Z']), Czx(['Z', 'X']), Ckz(['K', 'Z'])]

problem = CSP(variables=variables, domains=domains, constraints=constraints)
initial_state = {}

print('Pre-processing w/ AC3')
print(f'Domains before the pre-processing step: \n{problem.domains}')
optimizer = AC3(csp=problem)
optimizer.run(state=initial_state)
print(f'\ndomains after the pre-processing step: \n{problem.domains}')


search = BackTracking(problem=problem, var_criterion=degree_heuristic, value_criterion=least_constraining_value)
print('\n\nApply search using Backtracking algorithm')
print(search.run(state=initial_state))