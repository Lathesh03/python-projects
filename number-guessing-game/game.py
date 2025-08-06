import random
secret_number = random.randint(1, 100)
# print(secret_number) # You can uncomment this line for testing

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            break  # Exit the loop when the guess is correct
    except ValueError:
        print("Invalid input. Please enter a valid number.")