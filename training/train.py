"""
This file is used to train the Tensorflow model
"""
import tensorflow as tf
import numpy as np
import json
from sklearn.model_selection import train_test_split

# load_game_data, loads data from the simulations to learn from
def load_game_data(filename="connect4_games.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
# prepare_data, self explanatory
def prepare_data(games):
    X = []
    y = []
    for game in games:
        for move in game:
            # flatten each board state
            board_1d = np.array(move["board"]).flatten()
            # add the board state to the X field of the model
            X.append(board_1d)
            # add the result of the match to the Y field
            y.append(move["result"])
    # return the data as two numpy arrays
    return np.array(X, dtype=np.float32), np.array(y, dtype=np.float32)

# create_model, train the model with the information provided
def create_model(input_shape):
    # crazy tensorflow neural network magic
    # pretty sure its generating layers and nodes for descision making
    model = tf.keras.models.Sequential([
        tf.keras.layers.Input(shape=input_shape),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1, activation='tanh')
    ])
    return model

# create an instance of the game data and print information about it
games = load_game_data()
print(f"Number of games loaded: {len(games)}")
X, y = prepare_data(games)
print(f"Shape of X: {X.shape}")
print(f"Shape of y: {y.shape}")

# split the data using train_test_split from sci-kit learn
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# create the model with respect to the shape of the board (what we will use as input for move descision making)
model = create_model(X_train.shape[1:])
# compile and evaluate the model, more Tensorflow magic
model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))
loss = model.evaluate(X_val, y_val)
# print the validation loss and save the model
print(f"Validation Loss: {loss}")
model.save("connect4_model.keras")
