from ai.ai import AI

class TicTacToe:

    def __init__(self, ai):
        self.board = [None for _ in range(9)]
        self.current_player = 'X'
        self.ai: AI = ai
        self.moves = []

    
    def recreate(self):
        self.board = [None for _ in range(9)]
        self.current_player = 'X'
        self.moves = []

    def display_board(self):
        for i in range(0, 9, 3):
            row = [str(self.board[i+j]) if self.board[i+j] is not None else ' ' for j in range(3)]
            print('|'.join(row))


    def make_move(self, position):
        if self.board[position] is None:
            self.board[position] = self.current_player
            return True
        else:
            print("Invalid move. That position is already taken." + f"{position}")
            return False

    def check_win(self):
        # Check rows
        for row in range(3):
            if self.board[row*3] == self.board[row*3 + 1] == self.board[row*3 + 2] and self.board[row*3] is not None:
                return self.board[row*3]

        # Check columns
        for col in range(3):
            if self.board[col] == self.board[col + 3] == self.board[col + 6] and self.board[col] is not None:
                return self.board[col]

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] is not None:
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] and self.board[2] is not None:
            return self.board[2]

        return None

    def check_draw(self):
        return all(cell is not None for cell in self.board)

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def run(self):
        while True:
            if self.current_player == 'O' and self.ai:
                move = self.ai.predict(self.moves)
            else:

                self.display_board()
                move = input(f"Player {self.current_player}, enter your move (0-8): ")
                if not move.isdigit() or not 0 <= int(move) <= 8:
                    print("Invalid input. Please enter a number between 0 and 8.")
                    continue
                move = int(move)
            if self.make_move(move):
                self.moves.append(move)
                winner = self.check_win()
                if winner:
                    print(f"Player {winner} wins!")
                    break
                elif self.check_draw():
                    print("It's a draw!")
                    break
                else:
                    self.switch_player()

