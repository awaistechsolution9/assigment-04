import random

number_to_guess = random.randint(0, 99)

while True:
    guess = int(input("Enter a guess: "))
    
    if guess > number_to_guess:
        print("Your guess is too high")
    elif guess < number_to_guess:
        print("Your guess is too low")
    else:
        print(f"Congrats! The number was: {number_to_guess}")
        break
