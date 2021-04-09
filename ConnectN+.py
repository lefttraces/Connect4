class ConnectN:

    def __init__(self):
        self._grid = [[] for _ in range(7)]
        self._rows = 6
        self._connect = 4
        self._player = 0
        self._game_fin = 0
        print('\nWelcome!')
        self._name_1 = input('Player 1\'s name: ')
        self._name_2 = input('Player 2\'s name: ')
        self._player_names = {0: self._name_1, 1: self._name_2}
        print(self)
        _column = input(f'{self._player_names[0]}, choose a column (1-{len(self._grid)}) to drop your first disc: ')
        while not (_column in {str(x) for x in range(1, len(self._grid)+1)}):
            _column = input(f'You must choose a number 1-{len(self._grid)}: ')
        self.game(int(_column))

    def __repr__(self):
        def row(i):
            return '| ' + ' | '.join([self._grid[j][i] if len(self._grid[j]) > i else ' '
                                      for j in range(len(self._grid))]) + ' |'
        game_grid = '\n' + '\n'.join([row(i) for i in range(self._rows-1, -1, -1)]) + '\n'
        return game_grid.translate(game_grid.maketrans('01', 'XO'))

    def game(self, n):
        print(self.play(n - 1))
        if not self._game_fin:
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
