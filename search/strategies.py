import random


class BreadthFirst:
    def add_visited(self, state):
        pass

    def select(self, fringe, new_nodes):
        return new_nodes + fringe


class DepthFirst:
    def add_visited(self, state):
        pass

    def select(self, fringe, new_nodes):
        return fringe + new_nodes


class GraphBreadthFirst:
    def __init__(self):
        self.visited = set()

    def add_visited(self, state):
        self.visited.add(state)

    def select(self, fringe, new_nodes):
        fringe = new_nodes + fringe
        fringe = [n for n in fringe if n.state not in self.visited]
        return fringe


class GraphDepthFirst:
    def __init__(self):
        self.visited = set()

    def add_visited(self, state):
        self.visited.add(state)

    def select(self, fringe, new_nodes):
        fringe = fringe + new_nodes
        fringe = [n for n in fringe if n.state not in self.visited]
        return fringe


class DepthLimited:
    def __init__(self, limit):
        self.limit = limit

    def add_visited(self, state):
        pass

    def select(self, fringe, new_nodes):
        fringe = fringe + new_nodes
        fringe = [n for n in fringe if n.depth <= self.limit]
        return fringe


class GraphDepthLimited:
    def __init__(self, limit):
        self.limit = limit
        self.visited = set()

    def add_visited(self, state):
        self.visited.add(state)

    def select(self, fringe, new_nodes):
        fringe = fringe + new_nodes
        fringe = [n for n in fringe
                  if n.state not in self.visited and n.depth <= self.limit]
        return fringe


class GraphRandom:

    def __init__(self):
        self.visited = set()

    def add_visited(self, state):
        self.visited.add(state)

    def select(self, fringe, new_nodes):
        new_fringe = new_nodes + fringe
        new_fringe = [n for n in new_fringe if n.state not in self.visited]
        # shuffle fringe
        random.shuffle(new_fringe)
        return new_fringe


class GraphUniformCost:
    def __init__(self):
        self.visited = set()

    def add_visited(self, state):
        self.visited.add(state)

    def select(self, fringe, new_nodes):
        fringe = fringe + new_nodes
        fringe = [n for n in fringe if n.state not in self.visited]
        # sort fringe following the cost g(n)
        fringe = sorted(fringe, key=lambda x: -x.cost)
        return fringe


class Greedy:
    def __init__(self, problem):
        self.visited = set()
        self.problem = problem

    def add_visited(self, state):
        self.visited.add(state)

    def select(self, fringe, new_nodes):
        fringe = fringe + new_nodes
        fringe = [n for n in fringe if n.state not in self.visited]
        # sort fringe following the heuristic function h(n)
        fringe = sorted(fringe, key=lambda x: -self.problem.h(x.state))
        return fringe


class AStar:
    def __init__(self, problem):
        self.visited = set()
        self.problem = problem

    def add_visited(self, state):
        self.visited.add(state)

    def select(self, fringe, new_nodes):
        fringe = fringe + new_nodes
        fringe = [n for n in fringe if n.state not in self.visited]
        # sort fringe following the heuristic function and cost --> f(n) = h(n) + g(n)
        fringe = sorted(fringe, key=lambda x: -(self.problem.h(x.state)+x.cost))
        return fringe