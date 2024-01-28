from csp.problem import *
from csp.ac3 import AC3
from csp.contraints import DifferentValues

map_vars = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']
map_domains = {var: ['green', 'red', 'blue'] for var in map_vars}
map_cons = [DifferentValues(['WA', 'NT']),
            DifferentValues(['NT', 'WA']),
            DifferentValues(['WA', 'SA']),
            DifferentValues(['SA', 'WA']),
            DifferentValues(['SA', 'NT']),
            DifferentValues(['NT', 'SA']),
            DifferentValues(['SA', 'Q']),
            DifferentValues(['Q', 'SA']),
            DifferentValues(['SA', 'NSW']),
            DifferentValues(['NSW', 'SA']),
            DifferentValues(['SA', 'V']),
            DifferentValues(['V', 'SA']),
            DifferentValues(['Q', 'NT']),
            DifferentValues(['NT', 'Q']),
            DifferentValues(['NSW', 'Q']),
            DifferentValues(['Q', 'NSW']),
            DifferentValues(['V', 'NSW']),
            DifferentValues(['NSW', 'V'])
            ]

# Example 1
print('Example 1')
problem = CSP(variables=map_vars,
              domains=map_domains,
              constraints=map_cons)
state = problem.initial_state
optimizer = AC3(csp=problem)
optimizer.run(state)
print(problem.domains)


# Example 2
print('\nExample 2')
problem = CSP(variables=map_vars,
              domains=map_domains,
              constraints=map_cons)
act_state = {'WA': 'red', 'Q': 'green'}
problem.domains['WA'] = ['red']
problem.domains['Q'] = ['green']
optimizer = AC3(csp=problem)
print("Result: " + str(optimizer.run(state)))
print("Domains: " + str(problem.domains))
