from search.local_search import *
from search.problem import *
from search.strategies import *
from search.tree_search import TreeSearch

random.seed(13)

# formulate the problem
frog_problem = JumpingFrogsProblem(N=3)

print('GOAL-BASED SEARCH')
print('---------------------------------------------------------------------')
# search strategy
strategies = [AStar(problem=frog_problem), GraphDepthLimited(limit=120)]

# search algorithm (Tree Search / Graph Search)
for strategy in strategies:
    search = TreeSearch(problem=frog_problem, strategy=strategy)

    # run algorithm
    result, node = search.run()

    # display the solutions
    print(f'Problem: {type(frog_problem).__name__}')
    print(f'Strategy: {type(strategy).__name__}')
    print("Result: " + result)
    print("Goal: " + str(node.state))
    print("Path: " + str(node.path()))
    print("Cost: " + str(node.cost))
    print('---------------------------------------------------------------------')

print('LOCAL SEARCH')
print('---------------------------------------------------------------------')
# search strategy
searches = [HillClimbing(problem=frog_problem), SimulatedAnnealing(problem=frog_problem)]

# search algorithm (Tree Search / Graph Search)
for search in searches:

    # run algorithm
    result, state = search.run()

    # display the solutions
    print(f'Problem: {type(frog_problem).__name__}')
    print(f'Strategy: {type(search).__name__}')
    print("Result: " + result)
    print("Goal: " + str(node.state))
    print("Path: " + str(node.path()))
    print("Cost: " + str(node.cost))
    print('---------------------------------------------------------------------')