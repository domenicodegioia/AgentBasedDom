from search.problem import *
from search.local_search import *

# formulate the problem
problem = EightQueensProblem()

# search algorithm
search = HillClimbing(problem=problem)
# search = SimulatedAnnealing(problem=problem, max_time=1000, lam=0.01)
# search = Genetic(problem=problem, population=50, generations=100, p_mutation=0.1, gene_pool=list(range(8)))

# run algorithm
result, state = search.run()

# display the solutions
print("Approach: " + search.__class__.__name__)
print("Result: " + result)
print("Value: " + str(problem.value(state)))
print("State: " + str(state))
# problem.print_chess(state)
