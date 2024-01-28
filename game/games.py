import random


class Game:
    def __init__(self, initial_state, player):
        self.initial_state = initial_state
        self.player = player

    def actions(self, state):
        """
        Given a state return the list of possible actions
        @param state: a state of the game
        @return: a list
        """
        return []

    def result(self, state, action):
        """
        Given a state and an action returns the reached state
        @param state: a state of the game
        @param action: a possible action in the state
        @return: a new state
        """
        return []

    def successors(self, state):
        """
        Given a state returns the reachable states with the respective actions
        :param state: actual state
        :return: list of successor states and actions
        """
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def terminal_test(self, state):
        """
        Returns True if the state is a final state (the game is over), False otherwise
        @param state: a state of the game
        @return: True or False
        """
        return False

    def utility(self, state):
        """
        Given a state returns its utility
        @param state: a state of the game
        @return: a utility value
        """
        return 0

    def player_utility(self, state):
        """
        Given a state, returns the utility of the state from the view of the MAX or the MIN player
        @param state: a state
        @return: a utility value
        """
        if self.player == 'MAX':
            # for MAX player
            return self.utility(state)
        elif self.player == 'MIN':
            # for MIN player
            return -self.utility(state)
        else:
            raise ValueError

    def next_player(self):
        """
        Return the next player to move
        @return: MAX or MIN
        """
        if self.player == 'MAX':
            return 'MIN'
        else:
            return 'MAX'

    def play(self, player_one, player_two):
        """
        A function that simulates the game between two players
        @param player_one: function that models the first player
        @param player_two:  function that models the second player
        """
        state = self.initial_state
        players = [player_one, player_two]
        moves = []
        while True:
            for player in players:
                if self.terminal_test(state):
                    print('----- GAME OVER -----\n\n')
                    return moves
                self.display(state)
                move = player.next_move(state)
                state = self.result(state, move)
                self.display_move(state, move)
                moves.append((move, self.player))
                self.player = self.next_player()
                print('_____________________')

    def display(self, state):
        print('_____________________')
        print(self.player, 'in ', state)

    def display_move(self, state, move):
        print(self.player, f'--{move}--> ', state)


class DummyGame(Game):
    def __init__(self, initial_state=None, player='MAX'):
        if initial_state is None:
            initial_state = 'A'
        super(DummyGame, self).__init__(initial_state, player)
        self.initial_state = initial_state
        self.player = player

    def actions(self, state):
        """
        Given a state return the list of possible actions
        @param state: a state of the game
        @return: a list
        """
        actions = {
            'A': ['a1', 'a2', 'a3'],
            'B': ['b1', 'b2', 'b3'],
            'C': ['c1', 'c2', 'c3'],
            'D': ['d1', 'd2', 'd3'],
        }
        if state in actions:
            return actions[state]
        else:
            return []

    def result(self, state, action):
        """
        Given a state and an action returns the reached state
        @param state: a state of the game
        @param action: a possible action in the state
        @return: a new state
        """
        result = {
            'A': {
                'a1': 'B',
                'a2': 'C',
                'a3': 'D'},
            'B': {
                'b1': 'B1',
                'b2': 'B2',
                'b3': 'B3'},
            'C': {
                'c1': 'C1',
                'c2': 'C2',
                'c3': 'C3'},
            'D': {
                'd1': 'D1',
                'd2': 'D2',
                'd3': 'D3'},
        }
        return result[state][action]

    def terminal_test(self, state):
        """
        Returns True if the state is a final state (the game is over), False otherwise
        @param state: a state of the game
        @return: True or False
        """
        if state in ('B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D1', 'D2', 'D3'):
            return True
        else:
            return False

    def utility(self, state):
        """
        Given a state returns its utility
        @param state: a state of the game
        @return: a utility value (integer)
        """
        utility = {'B1': 3,
                   'B2': 12,
                   'B3': 8,
                   'C1': 2,
                   'C2': 4,
                   'C3': 6,
                   'D1': 14,
                   'D2': 5,
                   'D3': 2}
        return utility[state]


class FrogState:
    def __init__(self, board, to_move):
        self.board = board
        self.to_move = to_move


class JumpingFrogsGame(Game):
    def __init__(self, N, player='MAX'):
        initial_state = N*'L' + '.' + N*'R'
        super(JumpingFrogsGame, self).__init__(initial_state, player)
        self.initial_state = FrogState(board=initial_state, to_move='L')
        self.player = player

    def actions(self, state: FrogState):
        possible_actions = []

        if state.to_move == 'L':
            for i in range(len(state.board)):
                if state.board[i: i + 2] == 'L.':  # Slide for L
                    possible_actions.append((i, i + 1))
                elif state.board[i: i + 3] == 'LR.':  # Jump for L
                    possible_actions.append((i, i + 2))
        else:
            for i in range(len(state.board)):
                if state.board[i: i + 2] == '.R':  # Slide for R
                    possible_actions.append((i + 1, i))
                elif state.board[i: i + 3] == '.LR':  # Jump for R
                    possible_actions.append((i + 2, i))

        return possible_actions

    def result(self, state: FrogState, action):
        i, j = action
        result = list(state.board)
        result[i], result[j] = state.board[j], state.board[i]
        return FrogState(board=''.join(result), to_move=self.next_player())

    def terminal_test(self, state: FrogState):
        if state.board == self.initial_state.board[::-1]:
            return True
        else:
            return False

    def utility(self, state):
        if self.terminal_test(state) and not self.successors(state):
            if state.to_move == 'L':
                return 1
            else:
                return -1
        return 0

    def display(self, state: FrogState):
        print('_____________________')
        print(self.player, 'in ', state.board)

    def display_move(self, state: FrogState, move):
        print(self.player, f'--{move}--> ', state.board)


class TTTState:
    def __init__(self, board, to_move):
        self.board = board
        self.to_move = to_move

    def __repr__(self):
        # s = ''
        # s.join('\t')
        # s.join('\n___________________')
        #
        # for row in range(len(self.board)):
        #     s.join('|')
        #     for col in range(len(self.board)):
        #         if self.board[row][col] == 1:
        #             s.join('  X  ')
        #         elif self.board[row][col] == -1:
        #             s.join('  O  ')
        #         else:
        #             s.join('     ')
        #         s.join('|')
        #     s.join('\n')
        #     s.join('___________________')
        # return s
        return str(self.board)


class TicTacToe(Game):
    def __init__(self, initial_state=None, player='MAX'):
        if initial_state is None:
            board = [[None] * 3] * 3  # external list --> row, internal lists -> col
            initial_state = TTTState(board=board, to_move=1)
        super(TicTacToe, self).__init__(initial_state, player)
        self.initial_state = initial_state
        self.player = player

    def next_to_move(self, state: TTTState):
        return -1 if state.to_move == 1 else 1

    def actions(self, state: TTTState):
        possible_actions = [(row, col)
                            for row in range(len(state.board))
                            for col in range(len(state.board[row]))
                            if not state.board[row][col]]
        random.shuffle(possible_actions)
        return possible_actions

    def result(self, state: TTTState, action):
        row, col = action
        new_board = [list(state.board[i]) for i in range(len(state.board))]
        new_board[row][col] = state.to_move
        return TTTState(board=new_board, to_move=self.next_to_move(state))

    def check_winner(self, state: TTTState, player):
        row = any([all([
            state.board[i][j] == player
             for j in range(len(state.board[i]))]
            ) for i in range(len(state.board))
        ])
        col = any([all([
            state.board[j][i] == player
             for j in range(len(state.board[i]))]
            ) for i in range(len(state.board))
        ])
        diag1 = any([all([
            state.board[i][i] == player
            for i in range(len(state.board))
        ])])
        diag2 = any([all([
            state.board[i][len(state.board) - 1 - i] == player
            for i in range(len(state.board))
        ])])
        return any([row, col, diag1, diag2])

    def check_draw(self, state: TTTState):
        return sum([1 for row in range(len(state.board)) for col in range(len(state.board[row]))
                    if not state.board[row][col]]) == 0

    def terminal_test(self, state: TTTState):
        result_x = self.check_winner(state=state, player=1)
        result_o = self.check_winner(state=state, player=-1)
        draw = self.check_draw(state)
        return any([result_x, result_o, draw])

    def utility(self, state: TTTState):
        if self.check_winner(state, 1):
            return 1
        if self.check_winner(state, -1):
            return -1
        if self.check_draw(state):
            return 0
