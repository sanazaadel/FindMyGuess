def hint(user_guess: int, computer_guess: int):
    """Gives a hint to the user based on their guess compared to the computer's guess.
    """
    if user_guess < computer_guess:
        print("Your guess is too low!Try again. ")
    elif user_guess > computer_guess:
        print("Your guess is too high!Try again. ")
        
            
    