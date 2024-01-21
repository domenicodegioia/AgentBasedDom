from search.problem import *
from search.strategies import *
from search.tree_search import TreeSearch


# formulate the problem
initial_state = (2, 1, 4, 6, 3, 5)
pancake_problem = PancakeProblem(initial_state=initial_state)

# search strategy
strategies = [GraphBreadthFirst()]

# search algorithm (Tree Search / Graph Search)
for strategy in strategies:
    search = TreeSearch(problem=pancake_problem, strategy=strategy)

    # run algorithm
    result, node = search.recursive_run()

    # display the solutions
    print("Result: " + result)
    print("Goal: " + str(node.state))
    print("Path: " + str(node.path()))
    print("Path cost: " + str(node.cost))
