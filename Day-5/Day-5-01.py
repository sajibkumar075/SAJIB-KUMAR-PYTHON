import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        ch = int(input("Guess the number (1-100): "))
        attempts += 1
        if ch < number:
            print("Too low!")
        elif ch > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

play_game()