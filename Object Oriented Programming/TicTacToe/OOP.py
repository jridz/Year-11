class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Board:
    def __init__(self):
        self.cells = [[' ' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.cells:
            print(" | ".join(row))
            print("-" * 9)

    def mark_cell(self, row, col, symbol):
        if self.cells[row][col] == ' ':
            self.cells[row][col] = symbol
            return True
        else:
            return False

    def check_winner(self, symbol):
        # Check rows and columns
        for i in range(3):
            if all(self.cells[i][j] == symbol for j in range(3)) or all(self.cells[j][i] == symbol for j in range(3)):
                return True

        # Check diagonals
        if all(self.cells[i][i] == symbol for i in range(3)) or all(self.cells[i][2 - i] == symbol for i in range(3)):
            return True

        return False

    def is_board_full(self):
        return all(cell != ' ' for row in self.cells for cell in row)


class TicTacToeGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name, 'X')
        self.player2 = Player(player2_name, 'O')
        self.current_player = self.player1
        self.board = Board()

    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def play_game(self):
        while True:
            self.board.print_board()
            print(f"{self.current_player.name}'s turn ({self.current_player.symbol})")

            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))

            if self.board.mark_cell(row, col, self.current_player.symbol):
                if self.board.check_winner(self.current_player.symbol):
                    self.board.print_board()
                    print(f"{self.current_player.name} wins!")
                    break
                elif self.board.is_board_full():
                    self.board.print_board()
                    print("It's a tie!")
                    break

                self.switch_player()
            else:
                print("Cell already taken. Try again.")


if __name__ == "__main__":
    game = TicTacToeGame("Player 1", "Player 2")
    game.play_game()
