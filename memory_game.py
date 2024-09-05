import time
import random

def init_game() -> dict:
    cards = [' A', ' A', ' B', ' B', ' C', ' C', ' D', ' D', ' E', ' E', ' F', ' F', ' G', ' G', ' H', ' H']
    random.shuffle(cards)

    game_data = {
        'rows': 4,
        'columns': 4,
        'score': {'Player 1': 0, 'Player 2': 0},
        'turn': 'Player 1',
        'game_over': False,
        'board': [[" *" for _ in range(4)] for _ in range(4)],
        'cards_position': {i + 1: cards[i] for i in range(16)},
        'flipped': {},
        'matched': set(),
        'move_history': [],
    }
    return game_data

def display_board(board):
    print("  1  2  3  4")
    for i, row in enumerate(board, 1):
        print(f"{i}{' '.join(row)}")
    print()

def update_turn(game_data, board, choice1, choice2):
    print("No match. Try again.".center(30, "-"))
    time.sleep(1)
    board[choice1[0] - 1][choice1[1] - 1] = " *"
    board[choice2[0] - 1][choice2[1] - 1] = " *"
    game_data['turn'] = 'Player 2' if game_data['turn'] == 'Player 1' else 'Player 1'

def update_score(game_data, turn):
    game_data['score'][turn] += 1
    print(f"New Score is: {game_data['score']}\n")  # Print score after each match

def update_match(game_data, card_index1, card_index2, turn):
    game_data['matched'].add(card_index1)
    game_data['matched'].add(card_index2)

def check_game_over(game_data, matched, scores):
    if len(matched) == 16:
        print("Game Over!")
        print(f"Final Scores: {scores}")  # Final score only
        game_data['game_over'] = True
        return True
    return False

def play(game_data) -> None:
    board = game_data['board']
    cards_position = game_data['cards_position']
    matched = game_data['matched']
    scores = game_data['score']

    while not game_data['game_over']:
        display_board(board)
        turn = game_data['turn']
        print(f"{turn}'s turn: ".center(30,"="))

        # First card selection
        try:
            choice1 = tuple(map(int, input("Choose first card (X,Y): \n").split(",")))
            card_index1 = (choice1[0] - 1) * 4 + choice1[1]  # Calculate index from (row, col)
            if card_index1 in matched:
                print("This card is already matched. Choose a different card.")
                continue
            board[choice1[0] - 1][choice1[1] - 1] = cards_position[card_index1]
            display_board(board)
        except (ValueError, IndexError, KeyError):
            print("Invalid input. Please enter coordinates as X,Y within the grid.")
            continue

        # Second card selection
        while True:
            try:
                choice2 = tuple(map(int, input("Choose second card (X,Y): ").split(",")))
                card_index2 = (choice2[0] - 1) * 4 + choice2[1]
                if choice2 == choice1:
                    print("You cannot choose the same card twice. Choose a different card.")
                    continue
                if card_index2 in matched:
                    print("This card is already matched. Choose a different card.")
                    continue
                board[choice2[0] - 1][choice2[1] - 1] = cards_position[card_index2]
                break
            except (ValueError, IndexError, KeyError):
                print("Invalid input. Please enter coordinates as X,Y within the grid.")

        display_board(board)

        # Check for match
        if board[choice1[0] - 1][choice1[1] - 1] == board[choice2[0] - 1][choice2[1] - 1]:
            update_match(game_data, card_index1, card_index2, turn)

            # If it's not the last match, print the match message and update the score
            if not check_game_over(game_data, matched, scores):
                print("It's a match!".center(30, "-"))  # Only print match message if game isn't over
                update_score(game_data, turn)
                print(f"Keep going! It's {game_data['turn']}'s turn again!".center(50, "="))
        else:
            update_turn(game_data, board, choice1, choice2)


if __name__ == "__main__":
    game_data = init_game()
    play(game_data)

