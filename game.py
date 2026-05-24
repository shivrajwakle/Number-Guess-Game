import random

n = random.randint(1, 100)
guesses = 0

while True:
    try:
        a = int(input("Guess the number: "))
        guesses += 1

        if a > n:
            print("Please enter a smaller number")

        elif a < n:
            print("Please enter a higher number")

        else:
            print(f"Congratulations! You guessed the number {n} correctly in {guesses} attempts.")
            break

    except ValueError:
        print("Please enter a valid number")