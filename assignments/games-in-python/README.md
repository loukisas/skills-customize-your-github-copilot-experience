# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Implement a classic Hangman game in Python to practice string manipulation, loops, conditional logic, and user interaction.

## 📝 Tasks

### 🛠️ Word Selection and Game Setup

#### Description

Create the initial game setup by selecting a random word and preparing the game state.

#### Requirements
Completed program should:

- Define a predefined list of words and select one randomly using `random.choice()`.
- Initialize the hidden word display (e.g., `_ _ _ _`) based on the selected word length.
- Set maximum allowed incorrect attempts (e.g., 6).
- List used letters as the game progresses.

### 🛠️ Guess Processing and Game Loop

#### Description

Handle player guesses in a loop, updating display and managing incorrect/vs correct guesses.

#### Requirements
Completed program should:

- Prompt the player for one letter guess at a time.
- Validate input (single alphabetic character, not already guessed).
- Reveal matching letters in the display when guess is correct.
- Decrement remaining attempts for incorrect guesses.
- Show current state after each guess, for example:
  ```
  Word: h _ n g m a n
  Used letters: a, e, i
  Remaining attempts: 4
  ```

### 🛠️ Win/Loss Logic and Feedback

#### Description

Determine the game outcome and provide user feedback when the game is over.

#### Requirements
Completed program should:

- End the game with a win message when the user guesses all letters.
- End the game with a lose message when attempts reach zero and show the correct word.
- Print final user-friendly messages, e.g., `Congratulations, you won!` or `Game over. The word was: python`.
- Optionally, ask if the player wants to play again and restart the game loop.

