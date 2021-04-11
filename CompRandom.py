class ConnectN:

    def __init__(self):
        self._grid = [[] for _ in range(7)]
        self._rows = 6
        self._connect = 4
        self._player = 0
        self._game_fin = 0
        print('\nWelcome!')
        self._game_mode = input('Two player (2) OR v.s. computer (1)? ')
        while self._game_mode not in {'1', '2'}:
            self._game_mode = input('Enter (2) for two player OR (1) for v.s. computer: ')
        self._game_mode = int(self._game_mode)
        if self._game_mode == 2:
            self._name_1 = input('Player 1\'s name: ')
            self._name_2 = input('Player 2\'s name: ')
        elif self._game_mode == 1:
            self._name_1 = input('Player\'s name: ')
            self._name_2 = "Computer"
        self._player_names = {0: self._name_1, 1: self._name_2}
        print(self)
        if self._game_mode == 2 or self._player_names[0] != 'Computer':
            _first_column =\
                input(f'{self._player_names[0]}, choose a column (1-{len(self._grid)}) to drop your first disc: ')
            while not (_first_column in {str(x) for x in range(1, len(self._grid)+1)}):
                _first_column = input(f'You must choose a number 1-{len(self._grid)}: ')
        else:
            import random
            _first_column = random.randrange(1, len(self._grid)+1)
        self.game(int(_first_column))

    def __repr__(self):
        def row(i):
            return '| ' + ' | '.join([self._grid[j][i] if len(self._grid[j]) > i else ' '
                                      for j in range(len(self._grid))]) + ' |'
        game_grid = '\n' + '\n'.join([row(i) for i in range(self._rows-1, -1, -1)]) + '\n'
        return game_grid.translate(game_grid.maketrans('01', 'XO'))

    def game(self, n):
        import random
        print(self.play(n - 1))
        if not self._game_fin:
            if self._game_mode == 1 and self._player_names[self._player] == 'Computer':
                available_columns = [i+1 for i in range(len(self._grid)) if int(len(self._grid[i]) / self._rows) == 0]
                n = random.choice(available_columns)
                return self.game(n)
            else:
                n = input('Choose a column: ')
                while not (n in {str(x) for x in range(1, len(self._grid)+1)}):
                    n = input(f'You must choose a number 1-{len(self._grid)}: ')
                return self.game(int(n))

    def play(self, col):
        if len(self._grid[col]) < self._rows:
            self._grid[col].extend(str(self._player))
            self._player = (self._player + 1) % 2
            print(self)
        else:
            return 'Column full!'
        if (str(int((not self._player))) * self._connect in ''.join(self._grid[col])) \
                or (str(int((not self._player))) * self._connect in
                    ''.join([self._grid[i][len(self._grid[col]) - 1] if not (len(self._grid[i]) < len(self._grid[col]))
                             else' ' for i in range(len(self._grid))])) \
                or (str(int((not self._player))) * self._connect in
                    ''.join([self._grid[col-(len(self._grid[col])-1)+i][i]
                             if 0 <= col-(len(self._grid[col])-1)+i < len(self._grid)
                             and (len(self._grid[col-(len(self._grid[col])-1)+i]) >= i+1)
                             else ' 'for i in range(len(self._grid))])) \
                or (str(int((not self._player))) * self._connect in
                    ''.join([self._grid[i][col+(len(self._grid[col])-1)-i]
                             if 0 <= col+(len(self._grid[col])-1)-i < self._rows
                             and (len(self._grid[i]) >= col+(len(self._grid[col])-1)-i+1)
                             else ' ' for i in range(len(self._grid))])):
            self._game_fin = 1
            return f'{self._player_names[int((not self._player))]} wins!\n'
        if all([int(len(self._grid[i]) / self._rows) for i in range(len(self._grid))]):
            self._game_fin = 1
            return 'Game ends in draw'
        return f'{self._player_names[self._player]}\'s turn'


game = ConnectN()
