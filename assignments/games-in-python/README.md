
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build an interactive Hangman game that practices string manipulation, loops, conditionals, and user input handling.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description

Create the initial Hangman game setup by selecting a secret word and preparing the game state.

#### Requirements
Completed program should:

- Choose a secret word randomly from a predefined list
- Initialize the hidden word display with underscores for each letter
- Track the number of allowed incorrect guesses

### 🛠️ Letter Guessing and Progress Display

#### Description

Allow the player to guess letters and update the displayed progress after each guess.

#### Requirements
Completed program should:

- Prompt the player to guess a letter
- Reveal correctly guessed letters in the hidden word display
- Show the current progress in `_ _ _` format after each guess
- Ignore repeated guesses and notify the player if a letter was already tried

### 🛠️ Win/Lose Conditions and Game Flow

#### Description

Handle game completion with win and lose conditions and display the final result.

#### Requirements
Completed program should:

- Reduce remaining attempts for incorrect guesses
- End the game when the word is fully guessed or attempts run out
- Display a win message with the completed word when the player succeeds
- Display a loss message and reveal the secret word when attempts are exhausted

