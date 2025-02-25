# Connect-4 Neural Network Opponent

This Python repository contains a full text-based Connect 4 game and a basic AI opponent for single-player gameplay.  
The data used to train the model was created by simulating 5000 random games of Connect 4, the code for which can be found in the `training` folder.  
The model was created using TensorFlow and can be used to play against a human or another bot.

| ![alt text](res/example_board.png) |
|:--:|
| *A.1 An example board from the game.* |

### Gameplay

The game is played on a 7x6 board. Connect-4 is a 7;6;4 style m;n;k game, in which a player wins when they have 4 of their pieces in any type of line. Pieces are affected by gravity and will be placed on the lowest possible row of any column. The game is text based and an abstract version of the board is shown before each turn (see image A.1). The player can decide which column to place their piece.

### Generating Training Data

The data used to train the model was created by simulating 5000 different random games of connect 4. The simulations were created by pining two bots against eachother. The bots descision making was completely randomized, where they would pick a random valid column and place their piece there. This code can be found in the `Bot.py` file. The data from these games were stored in a json file and then loaded by the training script. My json file is far too large to include on GitHub so the provided one is empty.

### Training

The model generated is a neural network made with Tensorflow.

### Example Footage
Here is example footage of two bots playing against each other.
| ![](res/example_play.mp4) |
|:--:|
| *V.1 Two bots duking it out*|
