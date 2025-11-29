"""Function to provide hints based on user's guess."""


def hint(user_guess, computer_guess):
    if user_guess < computer_guess:
        print("Your guess is too low!Try again. ")
    elif user_guess > computer_guess:
        print("Your guess is too high!Try again. ")
        
            
    