class Connect4:

    def __init__(self):
        self.grid = [[], [], [], [], [], [], []]
        self.player = 0
        self.game_fin = 0

    def play(self, col):
        if self.game_fin:
            return 'Game has finished!'
        if len(self.grid[col]) < 6:
            self.grid[col].append(str(self.player))
            self.player = (self.player + 1) % 2
        else:
            return 'Column full!'
        if (str(int((not self.player))) * 4 in ''.join(self.grid[col])) \
                or (str(int((not self.player))) * 4 in
                    ''.join([self.grid[i][len(self.grid[col]) - 1] if not (len(self.grid[i]) < len(self.grid[col]))
                             else' ' for i in range(len(self.grid))])) \
                or (str(int((not self.player))) * 4 in
                    ''.join([self.grid[col-(len(self.grid[col])-1)+i][i]
                             if 0 <= col-(len(self.grid[col])-1)+i < len(self.grid)
                             and (len(self.grid[col-(len(self.grid[col])-1)+i]) >= i+1)
                             else ' 'for i in range(len(self.grid))])) \
                or (str(int((not self.player))) * 4 in
                    ''.join([self.grid[i][col+(len(self.grid[col])-1)-i]
                             if 0 <= col+(len(self.grid[col])-1)-i < 6
                             and (len(self.grid[i]) >= col+(len(self.grid[col])-1)-i+1)
                             else ' ' for i in range(len(self.grid))])):
            self.game_fin = 1
            return f'Player {int((not self.player)) + 1} wins!'
        return f'Player {int((not self.player)) + 1} has a turn'

