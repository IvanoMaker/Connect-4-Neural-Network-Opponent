import random
import tensorflow as tf
import numpy as np

# Bot class
class Bot:
    def __init__(self, process, model_path=None):
        # process, clarifies which descision making process is used
        self.process = process
        # model, if the bot uses an AI model, this links to the keras file
        self.model = None

        if process == "rand":
            self.process = process
        elif process == "model" and model_path: #add model loading.
            try:
                self.model = tf.keras.models.load_model(model_path)
            except Exception as e:
                print(f"Error loading model: {e}")

    # move, places a piece on the board
    def move(self, char, board):
        # random descision making process
        if self.process == "rand":
            # pick a random valid column
            cols = [1, 2, 3, 4, 5, 6, 7]
            choice = random.choice(cols)
            valid_move = False

            while not valid_move:
                temp = board.place(char, choice - 1)
                valid_move = temp
                if not temp:
                    # remove column from the options if it is full and repick
                    cols.remove(choice)
                    if not cols:
                        return None
                    choice = random.choice(cols)
                else:
                    break
            # return the placed column, or None if there is no option
            return choice

        # trained AI model descision making
        elif self.process == "model" and self.model:
            # determine valid columns
            valid_cols = [i+1 for i in range(7) if self.is_valid_move(board, char, i)]
            # return None if there are no valid columns
            if not valid_cols:
                return None
            # set best columns to non and the best value to negative infinity
            best_col = None
            best_val = -float('inf')
            # for each valid column
            for col in valid_cols:
                # create a copy of the board
                temp_board = board.copy()
                # if a piece is placed in the column
                if temp_board.place(char, col-1):
                    # Predict the conditiion of the board state and get the predicted value
                    temp_state = np.array(temp_board.encoded()).flatten().reshape(1, 42).astype(np.float32)
                    col_val = self.model.predict(temp_state)[0][0]
                    # if the column value is better than the current best value
                    if col_val > best_val:
                        # set both the 'best' variables
                        best_val = col_val
                        best_col = col
            # repeat until the best column is decided and return that column
            return best_col
        
    # is_valid_move, check to see if a move is valid without placing a piece on the board
    def is_valid_move(self, board, char, col):
        temp_board = board.copy()
        return temp_board.place(char, col)
