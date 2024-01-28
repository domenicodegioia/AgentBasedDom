from search.problem import AustraliaProblem
from search.local_search import *

nodes = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']
colors = ['r', 'g', 'b']

map_adjacent_nodes = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'V', 'SA'],
    'V': ['NSW', 'SA'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'T': []
}

problem = AustraliaProblem(initial_state={},
                           nodes=nodes,
                           colors=colors,
                           map_adjacent_nodes=map_adjacent_nodes)

searches = [HillClimbing(problem=problem),
            SimulatedAnnealing(problem=problem, max_time=1000, lam=0.01)]

for search in searches:
    result, state = search.run()
    print(f'\n{type(search).__name__}')
    print(f'result: {result}')
    print(f'value function: {problem.value(state)}')
    print(state)
