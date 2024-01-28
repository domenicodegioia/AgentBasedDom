import math
import random


class StreetProblem:

    def __init__(self, initial_state, goal_state, environment):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.environment = environment

    def successors(self, state):
        """
        Given a state returns the reachable states with the respective actions
        :param state: actual state
        :return: list of successor states and actions
        """
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def actions(self, state):
        """
        Given a state returns the list of possible actions
        :param state: actual state
        :return: a list of actions
        """
        return self.environment.streets[state]

    def result(self, state=None, action=None):
        """
        Given a state and an action returns the reached state
        :param state: actual state
        :param action: chosen action
        :return: reached state
        """
        return action

    def goal_test(self, state):
        """
        Checks if the goal condition has been reached
        :param state: actual state
        :return: True if the goal condition is matched, False otherwise
        """
        return state == self.goal_state

    def cost(self, state, action):
        """
        Given a state and an action returns the cost of the action
        :param state: a state
        :param action: an action
        :return: the cost of doing that action in that state
        """
        reached_state = self.result(state, action)
        return self.environment.distance(state, reached_state)

    def h(self, state):
        goal_x, goal_y = self.environment.coordinates[self.goal_state]
        x, y = self.environment.coordinates[state]
        return math.sqrt((goal_x - x) ** 2 + (goal_y - y) ** 2)


class EightTilesProblem:

    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    def successors(self, state):
        """
        Given a state returns the reachable states with the respective actions
        :param state: actual state
        :return: list of successor states and actions
        """
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def get_empty_tile(self, state):
        """
        Given a state returns the column and the row of the empty tile in the puzzle
        :param state: a state
        :return: a row and a column
        """
        pos = state.index(0)
        row = pos // 3
        col = pos % 3
        return row, col

    def actions(self, state):
        """
        Given a state returns the list of possible actions
        :param state: actual state
        :return: a list of actions
        """
        actions = []
        row, col = self.get_empty_tile(state)
        if row > 0:
            actions.append('Up')
        if row < 2:
            actions.append('Down')
        if col < 2:
            actions.append('Right')
        if col > 0:
            actions.append('Left')
        return actions

    def result(self, state=None, action=None):
        """
        Given a state and an action returns the reached state
        :param state: actual state
        :param action: chosen action
        :return: reached state
        """
        row, col = self.get_empty_tile(state)
        new_row = row
        new_col = col

        if action == 'Up':
            new_row = row - 1
        if action == 'Down':
            new_row = row + 1
        if action == 'Left':
            new_col = col - 1
        if action == 'Right':
            new_col = col + 1

        new_pos = new_row * 3 + new_col
        old_pos = row * 3 + col
        new_state = list(state)
        new_state[old_pos] = state[new_pos]
        new_state[new_pos] = 0

        return tuple(new_state)

    def goal_test(self, state):
        """
        Checks if the goal condition has been reached
        :param state: actual state
        :return: True if the goal condition is matched, False otherwise
        """
        return state == self.goal_state

    def cost(self, state, action):
        """
        Given a state and an action return the cost of the action
        :param state: a state
        :param action: a possible action
        :return: a cost
        """
        return 1

    def h(self, state):
        """
        Given a state return the value of the heuristic
        :param state: a state
        :return: the heuristic value
        """
        h = 0
        for index in range(8):
            if state[index] != self.goal_state[index]:
                h += 1
        return h

    @staticmethod
    def print(state):
        print('_____________')
        for i, n in enumerate(state):
            print('|', end='')
            if n == 0:
                n = 'x'
            print(f' {n} ', end='')
            if i % 3 == 2:
                print('|')
        print('_____________')


class EightQueensProblem:

    def __init__(self, initial_state=None):
        if initial_state is None:
            initial_state = self.random()
        self.initial_state = initial_state
        self.max_conflicts = sum([i for i in range(1, 8)])

    def successors(self, state):
        """
        Given a state returns the reachable states with the respective actions
        :param state: actual state
        :return: list of successor states and actions
        """
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def actions(self, state):
        """
        Given a state returns the list of possible actions
        :param state: actual state
        :return: a list of actions
        """
        actions = []
        for col, queen in enumerate(state):
            squares = list(range(0, 8))
            squares.remove(queen)
            new_actions = list(zip(squares, [col]*len(squares)))
            actions.extend(new_actions)
        return actions

    def result(self, state=None, action=None):
        """
        Given a state and an action returns the reached state
        :param state: actual state
        :param action: chosen action
        :return: reached state
        """
        new_state = list(state)
        col, new_row = action
        new_state[col] = new_row
        return tuple(new_state)

    def conflicts(self, state):
        """
        Given a state return the number of conflicts
        :param state: a state
        :return: number of conflicting queens
        """
        conflicts = 0
        for col in range(8):
            queen = state[col]
            for col1 in range(col+1, 8):
                queen1 = state[col1]

                if queen == queen1:
                    conflicts += 1
                if queen - col == queen1 - col1 or queen + col == queen1 + col1:
                    conflicts += 1
        return conflicts

    def goal_test(self, state):
        """
        Checks if the goal condition has been reached
        :param state: actual state
        :return: True if the goal condition is matched, False otherwise
        """
        return self.conflicts(state) == 0

    def cost(self, state, action):
        """
        Returns the cost of an action. In this problem the cost is always unitary.
        :param state: a state
        :param action: an action
        :return: a cost
        """
        return 1

    def value(self, state):
        """
        Returns the value of a state. This function is used for evaluating a state in the local search.
        (The higher the better)
        :param state: a state
        :return: the value of a state
        """
        return self.max_conflicts-self.conflicts(state)

    @staticmethod
    def random():
        """
        Generate a random chess with 8 queens
        :return: a tuple with 8 elements
        """
        chess = [random.randrange(0, 8) for _ in range(8)]
        return tuple(chess)

    @staticmethod
    def print_chess(state):
        print('\t', end='')
        for number in [1, 2, 3, 4, 5, 6, 7, 8]:
            print(f"|  {number}  ", end='')
        print('|', end='')
        print('\n\t_________________________________________________')

        for row, letter in zip(range(8), ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']):
            print(letter + '\t', end='')
            print('|', end='')

            for queen in state:
                if queen == row:
                    print('  Q  ', end='')
                else:
                    print('     ', end='')
                print('|', end='')
            print('\n', end='')
            print('\t_________________________________________________')


class GridProblem:
    """
    Finding a path on a 2D grid with obstacles. Obstacles are (x, y) cells.
    States:   (x, y) cell locations.
    Actions:  (dx, dy) cell movements.
    """

    def __init__(self, initial_state, goal_state, environment):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.environment = environment
        self.directions = [
            (-1, -1), (0, -1), (+1, -1),
            (-1, 0),           (+1,  0),
            (-1, +1), (0, +1), (+1, +1)
        ]

    def successors(self, state):
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def actions(self, state):
        x, y = state
        possible_actions = [(x+dx, y+dy) for (dx, dy) in self.directions]
        possible_actions = set(possible_actions) - self.environment.obstacles
        return possible_actions

    def result(self, state=None, action=None):
        return action if action not in self.environment.obstacles else state

    def goal_test(self, state):
        return state == self.goal_state

    def cost(self, state, action):
        new_state = self.result(state, action)
        return self.environment.straight_line_distance(state, new_state)

    def h(self, state):
        return self.environment.straight_line_distance(state, self.goal_state)


class PourProblem:
    """
    Finding a path on a 2D grid with obstacles.
    Obstacles are (x, y) cells.
    States: a tuple of current water levels.
    """

    def __init__(self, initial_state, goal_state, sizes):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.sizes = sizes

    def successors(self, state):
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def actions(self, state):
        possible_actions = []
        jugs = range(len(state))
        # (Fill, i): fill the ith jug all the way to the top (from a tap with unlimited water).
        possible_actions.append([('Fill',i) for i in jugs if state[i]<self.sizes[i]])
        # (Dump, i): dump all the water out of the ith jug.
        possible_actions.append([('Dump', i) for i in jugs])
        # (Pour, i, j): pour water from the ith jug into the jth jug until either the jug i is empty, or jug j is full,
        # whichever comes first.
        possible_actions.append([('Pour', i, j) for i in jugs if state[i] for j in jugs if i != j])
        return list(possible_actions)

    def result(self, state=None, action=None):
        a, i, *_ = action
        result = list(state)  # for initialization

        if a == 'Fill':
            result[i] = self.sizes[i]
        elif a == 'Dump':
            result[i] = 0
        elif a == 'Pour':
            j = action[2]
            amount = min(state[i], self.sizes[j] - state[j])
            result[i] -= amount
            result[j] += amount
        return tuple(result)

    def goal_test(self, state):
        return self.goal_state in state

    def cost(self, state, action):
        a, i, *_ = action
        return (self.sizes[i] - state[i]) if a == 'Fill' else 0

    def h(self, state):
        return self.environment.straight_line_distance(state, self.goal_state)


class PancakeProblem:
    """
    Given a stack of pancakes of various sizes, can you sort them into a stack of decreasing sizes,
    largest on bottom to smallest on top?
    """

    def __init__(self, initial_state, ):
        self.initial_state = initial_state
        self.goal_state = tuple(sorted(self.initial_state))

    def successors(self, state):
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def actions(self, state):
        return range(2, len(state) + 1)

    def result(self, state=None, action=None):
        new_state = list(state)
        top_i = [new_state[i] for i in range(action)]
        top_i.reverse()
        new_state = [new_state[i] for i in range(action, len(new_state))]
        return tuple(top_i + new_state)

    def goal_test(self, state):
        return state == self.goal_state

    def cost(self, state, action):
        return 1

    def h(self, state):
        return sum([state[i] == self.goal_state[i] for i in range(len(state))])


class JumpingFrogsProblem:
    """
    Finding a path on a 2D grid with obstacles. Obstacles are (x, y) cells.
    States:   (x, y) cell locations.
    Actions:  (dx, dy) cell movements.
    """

    def __init__(self, N):
        self.initial_state = N*'L' + '.' + N*'R'
        self.goal_state = self.initial_state[::-1]


    def successors(self, state):
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def actions(self, state):
        possible_actions = []
        for i in range(len(state)):
            if state[i : i+2] == 'L.':  # Slide for L
                possible_actions.append((i, i+1))
            elif state[i : i+3] == 'LR.':  # Jump for L
                possible_actions.append((i, i + 2))
            elif state[i : i+2] == '.R':  # Slide for R
                possible_actions.append((i+1, i))
            elif state[i : i+3] == '.LR':  # Jump for R
                possible_actions.append((i+2, i))
        return possible_actions

    def result(self, state=None, action=None):
        i, j = action
        result = list(state)
        result[i], result[j] = state[j], state[i]
        return ''.join(result)

    def goal_test(self, state):
        return state == self.goal_state

    def cost(self, state, action):
        return 1

    def h(self, state):
        # amount of locations different from the goal state (hamming distance)
        return sum(c1 != c2 for c1, c2 in zip(state, self.goal_state))

    def value(self, state):
        r = sum([1 for i in range(len(state) // 2) if state[i] == 'R']) - sum(
            [1 for i in range(len(state) // 2) if state[i] == 'L'])
        l = sum([1 for i in range(len(state) // 2 + 1, len(state)) if state[i] == 'L']) - sum(
            [1 for i in range(len(state) // 2 + 1, len(state)) if state[i] == 'R'])
        return r + l


class AustraliaProblem:
    def __init__(self, initial_state, nodes, colors, map_adjacent_nodes):
        self.initial_state = initial_state
        self.nodes = nodes
        self.colors = colors
        self.map_adjacent_nodes = map_adjacent_nodes

    def actions(self, state):
        possible_actions = [(node, color) for node in self.nodes for color in self.colors]
        random.shuffle(possible_actions)
        return possible_actions

    def result(self, state=None, action=None):
        node, new_color = action
        new_state = dict(state)
        new_state[node] = new_color
        return new_state

    def successors(self, state):
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def conflicts(self, state):
        conflicts = 0
        for node in state.keys():
            adjacent_nodes = [n for n in self.map_adjacent_nodes[node] if n in state.keys()]
            conflicts += sum([1 for n in adjacent_nodes if state[node] == state[n]])
        return conflicts / 2

    def goal_test(self, state):
        return len(state) == len(self.nodes) and self.conflicts(state) == 0

    def cost(self, state, action):
        return 1

    def value(self, state):
        return len(state) - self.conflicts(state)