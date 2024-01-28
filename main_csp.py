from csp.problem import *
from csp.backtracking import *
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

problem = CSP(variables=map_vars,
              domains=map_domains,
              constraints=map_cons)
search = BackTracking(problem=problem,
                      value_criterion=least_constraining_value)
initial_state = {}
print(search.run(initial_state))
