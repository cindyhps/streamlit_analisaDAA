import math

class SOSGame:
    def __init__(self, dimensions=3):
        self.dimensions = dimensions
        self.board = [[' ' for _ in range(dimensions)] for _ in range(dimensions)]
        self.current_player = None
        self.user_symbol = None
        self.bot_symbol = None

    def initialize_game(self, user_symbol):
        self.user_symbol = user_symbol
        self.bot_symbol = 'S' if user_symbol == 'O' else 'O'
        self.current_player = 'user' if user_symbol == 'O' else 'bot'

    def is_winner(self, symbol):
        for i in range(self.dimensions):
            if all([self.board[i][j] == symbol for j in range(self.dimensions)]) or \
               all([self.board[j][i] == symbol for j in range(self.dimensions)]):
                return True
        if all([self.board[i][i] == symbol for i in range(self.dimensions)]) or \
           all([self.board[i][self.dimensions-1-i] == symbol for i in range(self.dimensions)]):
            return True
        return False

    def is_board_full(self):
        return all([cell != ' ' for row in self.board for cell in row])

    def is_game_over(self):
        return self.is_winner(self.user_symbol) or self.is_winner(self.bot_symbol) or self.is_board_full()

    def get_empty_cells(self):
        return [(i, j) for i in range(self.dimensions) for j in range(self.dimensions) if self.board[i][j] == ' ']

    def user_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.user_symbol
            self.toggle_player()  # Toggle giliran setelah pemain memilih
            return True
        return False
 
    def bot_move(self, depth): #Menggunakan Alpha Beta Pruning
        best_score = -math.inf
        best_move = None
        alpha = -math.inf
        beta = math.inf

        for i, j in self.get_empty_cells():
            self.board[i][j] = self.bot_symbol
            score = self.minimax(depth, alpha, beta)
            self.board[i][j] = ' '
            if score > best_score:
                best_score = score
                best_move = (i, j)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break  # Alpha cut-off

        self.board[best_move[0]][best_move[1]] = self.bot_symbol
        self.toggle_player()


    def toggle_player(self):
        self.current_player = 'user' if self.current_player == 'bot' else 'bot'

    def minimax(self, depth, alpha, beta): 
        #Menggunakan Alpha Beta Pruning pada minimax
        if self.is_winner(self.user_symbol):
            return -1
        elif self.is_winner(self.bot_symbol):
            return 1
        elif self.is_board_full():
            return 0

        if self.current_player == 'bot':
            best_score = -math.inf
            for i, j in self.get_empty_cells():
                self.board[i][j] = self.bot_symbol
                score = self.minimax(depth - 1, alpha, beta)
                self.board[i][j] = ' '
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break  # Beta cut-off
            return best_score
        else:
            best_score = math.inf
            for i, j in self.get_empty_cells():
                self.board[i][j] = self.user_symbol
                score = self.minimax(depth - 1, alpha, beta)
                self.board[i][j] = ' '
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break  # Alpha cut-off
            return best_score
