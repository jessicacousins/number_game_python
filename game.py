import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    guess = None
    attempts = 0


    print("")
    print("******************************************************************")
    print("\nWelcome to Guess the Number Game!")
    print("Try to guess the number between 1 and 10 in the fewest possible attempts.")

    while guess != number_to_guess:
        try:
            guess = int(input("🟢 Make a guess: "))
            attempts += 1
            if guess < number_to_guess:
                print("Too low. Try again. ❌")
            elif guess > number_to_guess:
                print("Too high. Try again. ❌")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts! 🏆")
        except ValueError:
            print("Please enter a valid integer. 🚫")


if __name__ == "__main__":
    guess_the_number()

