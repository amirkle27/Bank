
def init_game() -> dict[any]:
    """
    Initializes the game data structure.

    Returns:
        dict: A dictionary containing game settings, including the number of rows and columns,
              player scores, the game board, and other necessary game state information.
    """
    rows, columns = 4, 4
    cards = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H']

    game_data = {
        'rows': rows,
        'columns': columns,
        'score': {'player1': 0, 'player2': 0},
        'turn': 'player1',
        'game_over': False,
        'board': prepare_board(rows, columns, cards),
        'move_history': []  # all of the card flips till now
    }
    return game_data


def prepare_board(rows, columns, cards) -> dict[any]:
    """
    Prepares the game board by shuffling cards and placing them into the board structure.

    Args:
        rows (int): Number of rows in the board.
        columns (int): Number of columns in the board.
        cards (list): List of card values to be placed on the board.

    Returns:
        dict: A dictionary representing the game board, where each key is a tuple (row, col)
              and the value is a dictionary with card information (card value, flipped state, matched state).
    """
    board = {}
    # shuffle the cards!
    # place the cards in the board- i.e.
    # board[(0, 0)] = {'card': 'A', 'flipped': False, 'matched': False}
    # board[(0, 1)] = {'card': 'B', 'flipped': False, 'matched': False}
    # ...
    # 1, 4
    # board[(1,4)]
    # { (0, 0): {'card': 'A', 'flipped': False, 'matched': False}
    #   (0, 1): {'card': 'B', 'flipped': True, 'matched': False} ... }
    return board

def play(game_data) -> None:
    """
    Runs the main game loop, handling player turns, guessing, and score updates.

    Args:
        game_data (dict): The game data dictionary containing the board, scores, and other game information.
    """
    while True:
        """
        demo code -- just for example of how to call functions 
        
        for player in [1, 2]:
            diaply_board(game_data)
            guess1 = get_valid_card(...)
            diaply_board(game_data)
            guess2 = get_valid_card(...)
            diaply_board(game_data)
            if match(guess1, guess2):
                score += 1
                play again
            else:
                flip_back_cards(..)
        """

"""        
  1 2 3 4
1 * * * A
2 * * * A
3 * * * B
4 * * * B
Player 1, play: 2 2
  1 2 3 4
1 * * * A
2 * C * A
3 * * * B
4 * * * B
Player 1, play: 2 3
  1 2 3 4
1 * * * A
2 * C D A
3 * * * B
4 * * * B
Player 2, play: 
  1 2 3 4
1 * * * A
2 * * * A
3 * * * B
4 * * * B
"""