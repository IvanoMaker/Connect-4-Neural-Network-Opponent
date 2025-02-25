from Board import *
from Bot import *

print("~ Welcome to Connect-4! ~")
print("     Bot Vs. Bot Mode    ")

# create board and bot objects
board = Board()
bot_1 = Bot("model", "training/connect4_model.keras")
bot_2 = Bot("model", "training/connect4_model.keras")

# main loop
while board.solved() == "#":
    # process bot 1's move
    bot_1_move = bot_1.move("X", board)
    if bot_1_move is not None:
        place_result = board.place("X", bot_1_move - 1)
        print(f"Bot 1 placed an X in column {bot_1_move}")
        print(board.draw())
    else:
        print("Bot 1 could not find a valid move. Game over.")
        break
    # process bot 2's move
    if board.solved() == "#":
        bot_2_move = bot_2.move("O", board)
        if bot_2_move is not None:
            place_result = board.place("O", bot_2_move - 1)
            print(f"Bot 2 placed an O in column {bot_2_move}")
            print(board.draw())
        else:
            print("Bot 2 could not find a valid move. Game over.")
            break
    else:
        break

# declare the winning bot victorious
print(f"~ {board.solved()} Wins! ~")
