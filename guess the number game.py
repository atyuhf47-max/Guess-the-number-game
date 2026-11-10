import random
print("Guess the number between 0 and 1000")
choices = list(range(0, 1001))
number = random.choice(choices)
user_input = int(input("Enter your guess: "))
while user_input != number:
 if user_input < number:
  print()
  print("Your guess is too low. Try again.")
 elif user_input > number:
  print()
  print("Your guess is too high. Try again.")
 user_input = int(input("Enter your guess again: "))
print()
print("Congratulations! You guessed the number correctly.")
print("The number was:", number)