import random
secret_number = random.randint(1, 100)
# print(secret_number) # You can uncomment this line for testing

while True:
    try:
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            break  # This must be indented to be part of the 'else' block
    except ValueError:
        print("Invalid input. Please enter a valid number.")