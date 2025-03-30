import random

#Simple number guessing game

number = random.randrange(100)
guess = -1

print("Guess a Number Game!\nGuess a number between 1 and 100")
while guess != number: 
    try:
        guess = int(input(f"Your guess: "))

    except ValueError:
        print("Invalid. Please enter a number")

    else:
        if guess == number:
            print(f"Congrats! Your guess is right! The number is {number}")
        
        elif guess not in range(1, 101):
            print("You can only input number within 1 - 100")
        
        elif guess < number:
            print("The number is higher than", guess)
        
        elif guess > number:
            print("The number is lower than", guess)
        