from search.problem import *
from search.strategies import *
from search.tree_search import TreeSearch
from input.grid import Grid

random.seed(13)

# load the environment
grid = Grid()

# formulate the problem
initial_state = (15, 30)
goal_state = (130, 30)
grid_problem = GridProblem(environment=grid,
                          initial_state=initial_state,
                          goal_state=goal_state)

# search strategy
strategies = [AStar(problem=grid_problem)]

# search algorithm (Tree Search / Graph Search)
for strategy in strategies:
    search = TreeSearch(problem=grid_problem, strategy=strategy)

    # run algorithm
    result, node = search.recursive_run()

    # display the solutions
    print("Result: " + result)
    print("Goal: " + str(node.state))
    print("Path: " + str(node.path()))
    print("Path cost: " + str(node.cost))
