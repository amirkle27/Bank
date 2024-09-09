from random import choice

import memory_game
import pytest
from memory_game import init_game, display_board, update_turn, update_match, check_game_over


@pytest.fixture

def game_data():
    return init_game()

def test_game_initialization (game_data):
    assert len(game_data ['cards_position']) == 16
    assert game_data['rows'] == 4
    assert game_data['columns'] == 4
    assert game_data['turn'] == 'Player 1'
    assert not game_data['game_over'] == True

def test_board_structure (game_data):
    board = game_data['board']
    assert len(board) == 4
    assert all(len(row) == 4 for row in board)

def test_choice1_choice2_not_same ():
    choice1 = (1,1)
    choice2 = (1,1)
    with pytest.raises(AssertionError) as ex:
        assert str(ex.value) == "Choices must not be the same"

def test_choice1_in_matched():
    choice1 = (1, 1)
    matched = [choice1]
    with pytest.raises(AssertionError) as ex:
        assert str(ex.value) == "One or both cards are already matched. Try again."

def test_choice2_in_matched():
    choice2 = (1, 1)
    matched = [choice2]
    with pytest.raises(AssertionError) as ex:
        assert str(ex.value) == "One or both cards are already matched. Try again."

def test_choice1_out_of_grid():
    game_data = init_game()
    choice1 = (5, 5)  # Out of bounds

    with pytest.raises(IndexError, match="Invalid input. Please enter coordinates as X,Y within the grid."):
        # This part should raise IndexError before trying to access `cards_position`
        if not (1 <= choice1[0] <= 4 and 1 <= choice1[1] <= 4):
            raise IndexError("Invalid input. Please enter coordinates as X,Y within the grid.")
        # If this condition is met, the game shouldn't continue
        card_index1 = (choice1[0] - 1) * 4 + choice1[1]
        game_data['board'][choice1[0] - 1][choice1[1] - 1] = game_data['cards_position'][card_index1]


def test_choice2_out_of_grid():
    game_data = init_game()
    choice2 = (5, 5)

    with pytest.raises(IndexError, match="Invalid input. Please enter coordinates as X,Y within the grid."):
        # This part should raise IndexError before trying to access `cards_position`
        if not (1 <= choice2[0] <= 4 and 1 <= choice2[1] <= 4):
            raise IndexError("Invalid input. Please enter coordinates as X,Y within the grid.")
        card_index2 = (choice2[0] - 1) * 4 + choice2[1]
        game_data['board'][choice2[0] - 1][choice2[1] - 1] = game_data['cards_position'][card_index2]

def test_choice_str_for_int(monkeypatch):
    game_data = init_game()
    inputs = iter (['a','1,1'])
    board = game_data['board']
    cards_position = game_data['cards_position']
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises (ValueError):
        try:
            choice1 = tuple(map(int, input("Choose first card (X,Y): \n").split(",")))
            card_index1 = game_data['card_index1']
            board[choice1[0] - 1][choice1[1] - 1] = cards_position[card_index1]
        except (ValueError, IndexError,KeyError) as e:
            raise ValueError(str(e))


def test_position_for_choice ():
    choice1 = (1,1)
    position = (choice1[0] - 1) * 4 + choice1[1]
    assert position == 1

def test_switch_turn ():
    game_data = init_game()
    turn = game_data['turn']
    choice1 = (1,1)
    choice2 = (2,2)
    game_data['board'][choice1[0] - 1][choice1[1] - 1] = 'A'
    game_data['board'][choice2[0] - 1][choice2[1] - 1] = 'B'
    update_turn(game_data, game_data['board'], choice1, choice2)
    assert game_data['turn'] == 'Player 2' if turn == 'Player 1' else 'Player 1'

def test_update_score ():
    from memory_game import update_score
    game_data = init_game()
    turn = game_data['turn']
    score = game_data['score'][turn]
    update_score(game_data, turn)
    assert game_data['score'][turn] == score +1

def test_update_match ():
    game_data = init_game()
    board = game_data['board']
    turn = game_data['turn']
    choice1 = (1, 1)
    choice2 = (2, 2)
    card_index1 = (choice1[0] - 1) * 4 + choice1[1]
    card_index2 = (choice2[0] - 1) * 4 + choice2[1]

    board[choice1[0] - 1][choice1[1] - 1] = 'A'
    board[choice2[0] - 1][choice2[1] - 1] = 'A'
    update_match(game_data, card_index1, card_index2, turn)
    assert card_index1 in game_data['matched']
    assert card_index2 in game_data['matched']

def test_check_game_over ():
    game_data = init_game()
    game_data['game_over'] = False
    game_data['matched'] = set(range(1,17))
    scores = game_data['score']
    game_over = check_game_over(game_data, game_data['matched'], scores)
    assert game_over == True
    assert game_data['game_over'] == True
