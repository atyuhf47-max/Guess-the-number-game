Guess the Number Game

A simple command-line game written in Python. The program picks a secret number between 0 and 1000, and you try to guess it. After each guess, you're told whether it was too low or too high until you get it right.

Requirements
Python 3.x
No external libraries (uses only the built-in random module)
How to Run
bash
python "guess the number game.py"
How to Play
The game picks a random number from 0 to 1000 (inclusive).
Enter your guess when prompted.
The game tells you if your guess is too low or too high.
Keep guessing until you find the number.
When you guess correctly, the game congratulates you and reveals the number.
Example Session
Guess the number between 0 and 1000
Enter your guess: 500

Your guess is too high. Try again.
Enter your guess again: 250

Your guess is too low. Try again.
Enter your guess again: 375

Congratulations! You guessed the number correctly.
The number was: 375
How It Works
random.choice(range) selects the secret number from a list of 0–1000.
A while loop repeats until the guess equals the secret number.
Each iteration compares the guess with the secret number and prints a hint.
Known Limitations
Entering anything other than a whole number (e.g. text or a decimal) will crash the program with a ValueError.
There is no limit on attempts and no guess counter.
Guesses outside 0–1000 are accepted without a warning.
Possible Improvements
Add input validation with try/except.
Count and display the number of attempts.
Add difficulty levels or a configurable range.
Offer a "play again" option.
Tip

A binary-search strategy (always guess the midpoint of the remaining range) will find any number in at most 10 guesses.
