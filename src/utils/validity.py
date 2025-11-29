def get_valid_input():
    while True:
        user_input = input("Guess a number between 1 and 100: ")
        if not user_input.isdigit():
            print("Invalid input. Please enter a number between 1 and 100.")
            continue
        value = int(user_input)
        if 1 <= value <= 100:
            return value
        print("Invalid input. Please enter a number between 1 and 100.")