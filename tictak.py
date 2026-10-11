import math

class TicTacToe:
    def __init__(self):
        # The board is represented as a list of 9 spots (0 to 8)
        self.board = [" " for _ in range(9)]
        self.human = "O"
        self.ai = "X"

    def print_board(self):
        print()
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print()

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                return True
        return False

    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all([s == letter for s in row]):
            return True

        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True

        # Check diagonals (only if the move is on a diagonal)
        if square % 2 == 0:
            diagonal1 = [self.board[0], self.board[4], self.board[8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[2], self.board[4], self.board[6]]
            if all([s == letter for s in diagonal2]):
                return True

        return False


def minimax(state, depth, is_maximizing, ai_player, human_player):
    # Base cases: evaluate terminal states
    # Check if human won
    if state.winner(last_move_check(state, ai_player), ai_player):
        return {'position': None, 'score': 1 * (state.num_empty_squares() + 1)}
    elif state.winner(last_move_check(state, human_player), human_player):
        return {'position': None, 'score': -1 * (state.num_empty_squares() + 1)}
    elif not state.empty_squares():
        return {'position': None, 'score': 0}

    if is_maximizing:
        max_eval = -math.inf
        best_square = None
        for possible_move in state.available_moves():
            state.board[possible_move] = ai_player
            sim_score = minimax(state, depth + 1, False, ai_player, human_player)
            state.board[possible_move] = " " # Undo move
            
            if sim_score['score'] > max_eval:
                max_eval = sim_score['score']
                best_square = possible_move
        return {'position': best_square, 'score': max_eval}
    else:
        min_eval = math.inf
        best_square = None
        for possible_move in state.available_moves():
            state.board[possible_move] = human_player
            sim_score = minimax(state, depth + 1, True, ai_player, human_player)
            state.board[possible_move] = " " # Undo move
            
            if sim_score['score'] < min_eval:
                min_eval = sim_score['score']
                best_square = possible_move
        return {'position': best_square, 'score': min_eval}

def last_move_check(state, letter):
    # Helper to find the last played move for win-checking
    for i, spot in enumerate(state.board):
        if spot != " ":
            # We check if this spot creates a win
            if state.winner(i, letter):
                return i
    return 0


def play_game():
    game = TicTacToe()
    print("Welcome to Tic-Tac-Toe!")
    print("Board layout (enter numbers 0-8):")
    print(" 0 | 1 | 2 ")
    print("---+---+---")
    print(" 3 | 4 | 5 ")
    print("---+---+---")
    print(" 6 | 7 | 8 \n")

    while game.empty_squares():
        # Human turn
        if game.human == "O":
            game.print_board()
            try:
                square = int(input("Your turn (0-8): "))
                if square not in game.available_moves():
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Please enter a valid number between 0 and 8.")
                continue

            if game.make_move(square, game.human):
                game.print_board()
                print("Congratulations, you win! (This shouldn't happen against Minimax!)")
                return
        
        if not game.empty_squares():
            break

        # AI turn
        print("AI is thinking...")
        if len(game.available_moves()) == 9:
            square = 0 # Opening book optimization: take a corner or center
        else:
            square = minimax(game, 0, True, game.ai, game.human)['position']

        if game.make_move(square, game.ai):
            game.print_board()
            print("AI wins! Better luck next time.")
            return

    game.print_board()
    print("It's a tie!")

if __name__ == '__main__':
    play_game()