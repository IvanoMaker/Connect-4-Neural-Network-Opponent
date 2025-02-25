import json
from ..Board import *
from ..Bot import *

# save_game_data, save data in a json file
def save_game_data(game_data, filename="connect4_games.json"):
    with open(filename, "w") as f:
        json.dump(game_data, f, indent=4)

# load_game_data, load data from a json file
def load_game_data(filename="connect4_games.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# charMap, map X and O to 1 and -1 respectively, 0 otherwise
def charMap(a):
    if a == "X":
        return 1
    elif a == "O":
        return -1
    else:
        return 0

# run, main game loop that faces two bots against eachother
def run():
    board = Board()
    game = []
    moveCounter = 0

    # Bots can have two process types
    # Bot("rand") and Bot("Model")
    #   * rand, short for random, will make the bot randomly pick a valid row and palce there (used in early development)
    #   * model, uses the tensorflow model to determine the highest value move

    player_1 = Bot("rand")
    player_2 = Bot("rand")

    # While the board is not solved (no one has won)
    while board.solved() == "#":
        # check for a tie
        if board.tie():
            print("~ Tie! ~")
            return game  # Return the game data even in a tie
        
        # mark the first players move, return the row the player placed in
        c_1 = player_1.move("X", board)

        # append the move data to the game list
        game.append({
            "player": 1,
            "col": c_1,
            "board": board.encoded(),
            "result": 0,
        })

        # increment counter
        moveCounter += 1

        # repete the previous steps for player 2
        if board.solved() == "#":
            if board.tie():
                print("~ Tie! ~")
                return game
            
            c_2 = player_2.move("O", board)

            game.append({
                "player": -1,
                "col": c_2,
                "board": board.encoded(),
                "result": 0,
            })
            moveCounter += 1
        else:
            break

    # display who wins
    print(f"~ {board.solved()} Wins! ~")

    # map the winner to the encoded number
    outcome = charMap(board.solved())
    # mark the "result" of each move based on if the player won the game (1, player from that move won, -1 player from that move lost)
    for move in game:
        if move["player"] == 1:
            move["result"] = outcome
        else:
            move["result"] = -outcome
    return game

# Load existing games (if any)
all_games = load_game_data()

# Generate 1000 games for the model to observe
num_games_to_play = 1000

for _ in range(num_games_to_play):
    game_data = run()
    all_games.append(game_data)

# Save all games to the JSON file
save_game_data(all_games)
print(f"Ran {num_games_to_play} simulated games successfully.")
