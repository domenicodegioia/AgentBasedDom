from search.problem import *
from search.strategies import *
from search.tree_search import TreeSearch


# formulate the problem
initial_state = (0,0,0)
goal_state = 13
sizes = (2, 16, 32)
pour_problem = PourProblem(initial_state=initial_state,
                           goal_state=goal_state,
                           sizes=sizes)

# search strategy
strategies = [GraphRandom(),
              AStar(problem=pour_problem)]

# search algorithm (Tree Search / Graph Search)
for strategy in strategies:
    search = TreeSearch(problem=pour_problem, strategy=strategy)

    # run algorithm
    result, node = search.recursive_run()

    # display the solutions
    print("Result: " + result)
    print("Goal: " + str(node.state))
    print("Path: " + str(node.path()))
    print("Path cost: " + str(node.cost))
