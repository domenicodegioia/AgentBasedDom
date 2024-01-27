from search.problem import *
from search.strategies import *
from search.tree_search import TreeSearch
from input.grid import Grid

random.seed(13)

# formulate the problem
frog_problem = JumpingFrogsProblem(N=3)

# search strategy
strategies = [AStar(problem=frog_problem)]

# search algorithm (Tree Search / Graph Search)
for strategy in strategies:
    search = TreeSearch(problem=frog_problem, strategy=strategy)

    # run algorithm
    result, node = search.recursive_run()

    # display the solutions
    print("Result: " + result)
    print("Goal: " + str(node.state))
    print("Path: " + str(node.path()))
    print("Path cost: " + str(node.cost))
