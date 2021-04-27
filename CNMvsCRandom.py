class ConnectN:

    def __init__(self, columns=7, rows=6, connect=4):
        self._columns = columns
        self._rows = rows
        self._connect = connect
        self._grid = [[] for _ in range(self._columns)]
        self._player = 0
        self._game_fin = 0
        self._winner = None
        self._name_1 = "Computer1"
        self._name_2 = "Computer2"
        self._player_names = {0: self._name_1, 1: self._name_2}
        import random
        first_column = random.randrange(1, len(self._grid) + 1)
        self.game(first_column)

    @property
    def winner(self):
        return self._winner

    def __repr__(self):
        def row(i):
            return '| ' + ' | '.join([self._grid[j][i] if len(self._grid[j]) > i else ' '
                                      for j in range(len(self._grid))]) + ' |'

        game_grid = '\n' + '\n'.join([row(i) for i in range(self._rows - 1, -1, -1)]) + '\n'
        return game_grid.translate(game_grid.maketrans('01', 'XO'))

    def game(self, n):

        self.play(n - 1)

        if not self._game_fin and self._player == 0:

            import random
            import copy
            available_columns = [i + 1 for i in range(len(self._grid)) if int(len(self._grid[i]) / self._rows) == 0]

            grid_copy = copy.deepcopy(self._grid)
            player_name = self._player_names[self._player]
            for col in available_columns:
                if self.play(col - 1) == player_name:
                    self._grid = copy.deepcopy(grid_copy)
                    self._player = (self._player + 1) % 2
                    self._game_fin = 0
                    return self.game(col)
                self._grid = copy.deepcopy(grid_copy)
                self._player = (self._player + 1) % 2
                self._game_fin = 0

            self._player = (self._player + 1) % 2
            grid_copy = copy.deepcopy(self._grid)
            player_name = self._player_names[self._player]
            for col in available_columns:
                if self.play(col - 1) == player_name:
                    self._grid = copy.deepcopy(grid_copy)
                    self._game_fin = 0
                    return self.game(col)
                self._grid = copy.deepcopy(grid_copy)
                self._player = (self._player + 1) % 2
                self._game_fin = 0

            self._player = (self._player + 1) % 2
            current_player = self._player
            grid_copy = copy.deepcopy(self._grid)
            for col in available_columns:
                if len(self._grid[col - 1]) < self._rows - 1:
                    self.play(col - 1)
                    player_name = self._player_names[self._player]
                    if self.play(col - 1) == player_name:
                        self._game_fin = 0
                        available_columns.remove(col)
                self._player = current_player
                self._grid = copy.deepcopy(grid_copy)

            current_player = self._player
            grid_copy = copy.deepcopy(self._grid)
            for col in available_columns:
                if len(self._grid[col - 1]) < self._rows - 1:
                    self.play(col - 1)
                    self._player = (self._player + 1) % 2
                    player_name = self._player_names[self._player]
                    if self.play(col - 1) == player_name:
                        self._game_fin = 0
                        self._player = (self._player + 1) % 2
                        self._grid = copy.deepcopy(grid_copy)
                        return self.game(col)
                self._player = current_player
                self._grid = copy.deepcopy(grid_copy)

            self._player = (self._player + 1) % 2
            grid_copy = copy.deepcopy(self._grid)
            for col in available_columns:
                if len(self._grid[col - 1]) != 0:
                    connected_then = ''.join([self._grid[i][len(self._grid[col - 1]) - 1] if not (
                            len(self._grid[i]) < len(self._grid[col - 1]))
                                              else ' ' for i in range(len(self._grid))]).count(
                        str(self._player) * (self._connect - 1))
                else:
                    connected_then = 0
                self.play(col - 1)
                connected_now = ''.join([self._grid[i][len(self._grid[col - 1]) - 1] if not (
                        len(self._grid[i]) < len(self._grid[col - 1]))
                                         else ' ' for i in range(len(self._grid))]).count(
                    str(int(not self._player)) * (self._connect - 1))
                if connected_now > connected_then and col != 1 and col != len(self._grid):
                    self._grid = copy.deepcopy(grid_copy)
                    self._game_fin = 0
                    return self.game(col)
                self._grid = copy.deepcopy(grid_copy)
                self._player = (self._player + 1) % 2
                self._game_fin = 0

            self._player = (self._player + 1) % 2
            grid_copy = copy.deepcopy(self._grid)
            for col in available_columns:
                if len(self._grid[col - 1]) != 0:
                    connected_then = ''.join([self._grid[i][len(self._grid[col - 1]) - 1] if not (
                            len(self._grid[i]) < len(self._grid[col - 1]))
                                              else ' ' for i in range(len(self._grid))]).count(
                        str(self._player) * (self._connect - 1))
                else:
                    connected_then = 0
                self.play(col - 1)
                connected_now = ''.join([self._grid[i][len(self._grid[col - 1]) - 1] if not (
                        len(self._grid[i]) < len(self._grid[col - 1]))
                                         else ' ' for i in range(len(self._grid))]).count(
                    str(int(not self._player)) * (self._connect - 1))
                if connected_now > connected_then and col != 1 and col != len(self._grid):
                    self._grid = copy.deepcopy(grid_copy)
                    self._player = (self._player + 1) % 2
                    self._game_fin = 0
                    return self.game(col)
                self._grid = copy.deepcopy(grid_copy)
                self._player = (self._player + 1) % 2
                self._game_fin = 0

            if available_columns:
                n = random.choice(available_columns)
            else:
                n = random.choice(range(1, self._columns + 1))
            return self.game(n)

        if not self._game_fin and self._player == 1:
            import random
            import copy

            available_columns = [i + 1 for i in range(len(self._grid)) if int(len(self._grid[i]) / self._rows) == 0]

            n = random.choice(available_columns)
            return self.game(n)

    def play(self, col):
        self._grid[col].extend(str(self._player))
        self._player = (self._player + 1) % 2
        if (str(int((not self._player))) * self._connect in ''.join(self._grid[col])) \
                or (str(int((not self._player))) * self._connect in
                    ''.join([self._grid[i][len(self._grid[col]) - 1] if not (len(self._grid[i]) < len(self._grid[col]))
                             else ' ' for i in range(len(self._grid))])) \
                or (str(int((not self._player))) * self._connect in
                    ''.join([self._grid[col - (len(self._grid[col]) - 1) + i][i]
                             if 0 <= col - (len(self._grid[col]) - 1) + i < len(self._grid)
                             and (len(self._grid[col - (len(self._grid[col]) - 1) + i]) >= i + 1)
                             else ' ' for i in range(len(self._grid))])) \
                or (str(int((not self._player))) * self._connect in
                    ''.join([self._grid[i][col + (len(self._grid[col]) - 1) - i]
                             if 0 <= col + (len(self._grid[col]) - 1) - i < self._rows
                             and (len(self._grid[i]) >= col + (len(self._grid[col]) - 1) - i + 1)
                             else ' ' for i in range(len(self._grid))])):
            self._game_fin = 1
            self._winner = self._player_names[int((not self._player))]
            return self._winner
        if all([int(len(self._grid[i]) / self._rows) for i in range(len(self._grid))]):
            self._game_fin = 1
            self._winner = "Draw"



