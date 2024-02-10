import numpy as np

from search.problem import VacuumWorldProblem
from search.strategies import *
from search.tree_search import TreeSearch

n = 3
initial_state = tuple(np.ones((n, n)).flatten())
goal_state = tuple(np.zeros((n, n)).flatten())
vacuum_position = tuple((0, 0))
problem = VacuumWorldProblem(initial_state, goal_state, vacuum_position)

# search strategy
strategies = [AStar(problem=problem)]

# search algorithm (Tree Search / Graph Search)
for strategy in strategies:
    search = TreeSearch(problem=problem, strategy=strategy)

    # run algorithm
    result, node = search.recursive_run()

    # display the solutions
    print("Result: " + result)
    print("Goal: " + str(node.state))
    print("Path: " + str(node.path()))
    print("Path cost: " + str(node.cost))
