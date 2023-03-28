import random
import time

print("Welcome, I am going to pick a number between 1 and 100")
time.sleep(3)
print("I am now picking a number...")
time.sleep(3)
guess = int(input("What is your guess? "))

correct_number = random.randint(1,100)

guess_count = 1

while guess != correct_number:
  guess_count += 1

  if guess < correct_number:
    guess = int(input("Wrong, You need to guess higher. What is your guess? "))
  else:
    guess = int(input("Wrong, You need to guess lower. What is your guess? "))



print(f"You got the right answer! the right answer was {correct_number}. It took {guess_count} tries.")



