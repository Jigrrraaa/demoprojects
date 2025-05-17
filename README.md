# Python Mini Games

This repository contains simple Python games for learning and fun.

## Games Included

### 1. Dice Rolling Game (`python-projects/dice_rolling_game.py`)

- Lets the user choose how many dice to roll.
- Asks for confirmation before rolling.
- Displays the result in parentheses (e.g., `(3, 5, 2)`).
- Tracks and displays the number of times dice have been rolled.
- Handles invalid input gracefully.

### 2. Number Guessing Game (`python-projects/number_guessing_game.py`)

- User 1 selects a secret number between 1 and 100.
- The terminal is cleared after the number is chosen.
- User 2 tries to guess the number.
- Gives hints:
  - "You are almost there" if the guess is within 5 numbers of the choice (but not equal).
  - "Too High" or "Too low" otherwise.
  - "Congratulations!" on a correct guess.
- Handles invalid input gracefully.

### 3. QR Code Generator (`python-projects/qr_code_generator.py`)

- Prompts the user to enter text or a URL.
- Prompts for a filename.
- Generates a QR code image and saves it as a PNG file.
- Requires the `qrcode` Python package (`pip install qrcode`).

### 4. Rock Paper Scissors Game (`python-projects/rock_paper_scissors_game.py`)

- Lets the user play Rock, Paper, Scissors against the computer.
- Uses emojis for a fun display.
- Handles invalid input and allows repeated play until the user quits.

## How to Run

1. Make sure you have Python 3 installed.
2. Open a terminal in this folder.
3. Run a game with:
   ```sh
   python python-projects/dice_rolling_game.py
   ```
   or
   ```sh
   python python-projects/number_guessing_game.py
   ```
   or
   ```sh
   python python-projects/qr_code_generator.py
   ```
   or
   ```sh
   python python-projects/rock_paper_scissors_game.py
   ```

## Requirements

- Python 3.x
- For QR code generator: `pip install qrcode`

---

Enjoy playing and learning!
