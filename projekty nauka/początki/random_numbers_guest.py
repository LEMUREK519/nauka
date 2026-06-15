import random

lowest_num = 1
highest_num = 1000
answer = random.randint(lowest_num, highest_num)
guesses = 0

is_running = True

print(" Welcome to the number guessing game!")
print(f"I'm thinking of a number between {lowest_num} and {highest_num}.")

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
           print("out of range!")
        elif guess < answer:
            print("Too low!")
        elif guess > answer:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {guesses} guesses.")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Please enter a valid number.")
        print(f"Please enter a number between {lowest_num} and {highest_num}.")