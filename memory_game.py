
import time


def init_game() -> dict[any]:
    """
    Initializes the game data structure.

    Returns:
        dict: A dictionary containing game settings, including the number of rows and columns,
              player scores, the game board, and other necessary game state information.
    """
    rows = 4
    columns = 4
    cards = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H']
    board,location,cards_position = prepare_board(rows,columns,cards)


    game_data = {
        'rows': rows,
        'columns': columns,
        'score': {'Player 1': 0, 'Player 2': 0},
        'turn': 'Player 1',
        'game_over': False,
        'board': board,
        'cards': cards,
        'location': location,
        'cards_position': cards_position,
        'flipped': {},
        'matched': set(),
        'move_history': []
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
    import random
    random.shuffle (cards)
    board = [["*" for _ in range(columns)] for _ in range(rows)]
    location = {(i + 1, j + 1): i * rows + j for i in range(rows) for j in range(columns)}
    cards_position = {i: cards[i] for i in range(rows * columns)}

    return board,location,cards_position





    # shuffle the cards!
    # place the cards in the board- i.e.
    # board[(0, 0)] = {'card': 'A', 'flipped': False, 'matched': False}
    # board[(0, 1)] = {'card': 'B', 'flipped': False, 'matched': False}
    # ...
    # 1, 4
    # board[(1,4)]
    # { (0, 0): {'card': 'A', 'flipped': False, 'matched': False}
    #   (0, 1): {'card': 'B', 'flipped': True, 'matched': False} ... }

def display_board (board):
    print(" 1 2 3 4")
    for i, row in enumerate(board, 1):
        print(f"{i}{' '.join(row)}")

def play(game_data) -> None:
    """
    Runs the main game loop, handling player turns, guessing, and score updates.

    Args:
        game_data (dict): The game data dictionary containing the board, scores, and other game information.
    """
    board = game_data['board']
    location = game_data['location']
    cards_position = game_data['cards_position']
    flipped = game_data['flipped']
    matched = game_data['matched']
    scores = game_data['score']
    turn = game_data['turn']
    move_history = game_data['move_history']
    rows = game_data['rows']
    columns = game_data['columns']

    while game_data['game_over'] == False:

        display_board(board)

        print(f"{turn}'s turn: ")
        try:
            choice1 = tuple(map(int,input("\nPlease choose a card to flip on the grid (X,Y): \n").split(",")))
            index1 = location[choice1]
            board[choice1[0] - 1][choice1[1] - 1] = cards_position[index1]
            if not choice1 in matched:
                board[choice1[0]-1][choice1[1]-1] = cards_position [index1]
                flipped[choice1] = cards_position[index1]
            else:
                print("\nThis card is already matched\n")
                continue
            display_board(board)
            choice2 = tuple(map(int,input("\nPlease choose a second card to flip on the board (X,Y): \n").split(",")))
            index2 = location[choice2]
            if not choice2 in flipped and not choice2 in matched:
                board[choice2[0] - 1][choice2[1] - 1] = cards_position[index2]
                flipped[choice2] = cards_position[index2]
            else:
                print("\nThis card is already flipped or matched\n")
                continue
            display_board(board)
            if cards_position[index1] == cards_position[index2]:
                print("\nThat's a match!\n")
                matched.add(choice1)
                matched.add(choice2)
                scores[turn] += 1

            else:
                print("\nNo match...\n")
                time.sleep(2)
                board[choice1[0]-1][choice1[1]-1] = "*"
                board[choice2[0]-1][choice2[1]-1] = "*"
                del flipped[choice1]
                del flipped[choice2]
        except:
            print("Something went wrong. Try again")
            continue

        game_data['move_history'].append({
            'Player': turn,
            'Choice 1': choice1,
            'Choice 2': choice2,
            'Match': cards_position[index1]==cards_position[index2]
        })

        if len(matched) == len(game_data['cards']):
            print(f"\nGame Over! Final Score: {scores}\n")
            again = input("\nPlay again?\n")
            if again.lower() in ['n','no']:
                print("\nToo bad. Goodbye and have a sweet and wonderful day!\n")
                game_data['game_over'] = True
                break
            elif again.lower() in ['y','yes']:
                print("\nWonderful!\n")
                game_data['game_over'] = False
                game_data.update(init_game())
            else:
                print("\nWrong key!\n")
                continue

        turn = 'Player 2' if turn == 'Player 1' else 'Player 1'
        game_data['turn'] = turn

if __name__ == "__main__":
    game_data = init_game()
    play(game_data)
