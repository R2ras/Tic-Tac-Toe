class TicTacToe:
    def __init__(self):
        self.cells = list(' ' * 9)
        self.winning_combinations = [
            list(range(0, 9, 3)),
            list(range(1, 9, 3)),
            list(range(2, 9, 3)),
            list(range(3)),
            list(range(3, 6)),
            list(range(6, 9)),
            list(range(0, 9, 4)),
            list(range(2, 7, 2)),

        ]
        self.current_player = 'X'
        self.winner = False
        self.moves_counter = 0
        self.game()

    def board_printer(self):
        """Function to print the board."""
        cell = self.cells
        print('---------')
        print('|', cell[0], cell[1], cell[2], '|')
        print('|', cell[3], cell[4], cell[5], '|')
        print('|', cell[6], cell[7], cell[8], '|')
        print('---------')

    def new_coordinates(self):
        """Function adds new coordinate for one of the player."""
        while True:
            coordinates = input('Enter the coordinates: ')
            as_list = coordinates.split(' ')
            try:
                as_list_int = list(map(int, as_list))
            except ValueError:
                print('You should enter numbers!')
                continue
            if not all(0 < i < 4 for i in as_list_int):
                print('Coordinates should be from 1 to 3!')
            else:
                row, column = as_list_int
                index = (((row - 1) * 3) + (column + 2) - 3)
                if self.cells[index] != ' ':
                    print('This cell is occupied! Choose another one!')
                else:
                    self.cells[index] = self.current_player
                    break

    def check_winner(self):
        """Function checks if current player won the game."""
        if any(all(self.current_player == self.cells[i] for i in line) for line in self.winning_combinations):
            self.winner = True
            print(self.current_player, 'wins')

    def change_players(self):
        """Function change player."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def game(self):
        """Function will start the game."""
        self.board_printer()
        while self.moves_counter < 9 and not self.winner:
            self.new_coordinates()
            self.moves_counter += 1
            self.board_printer()
            self.check_winner()
            self.change_players()
        if not self.winner:
            print('Draw')


TicTacToe()
