import random
from utils.validity import get_valid_input
from logic.hint import hint
from logic.scorer import Scorer 


def play_round():
    """Runs a single round of the number guessing game.
    """
    
    computer_guess = random.randint(1, 100)
    score = Scorer()
    while True:
        user_guess = get_valid_input()
        if computer_guess==user_guess:
            print("Congratulations! You've guessed the correct number! Do you want to play again? (yes/no): ")
            print(f"Your final score is: {score.get_score()}")
            break
        else:
            hint(user_guess, computer_guess)  
            score.update_score()
            print(f"Incorrect guess. Your current score is: {score.get_score()}")
            
            
def main():
        while True:
            play_round()
            replay = input("Do you want to play again? (yes/no): ")
            if replay.lower() in ['yes', 'y']:
                    continue
            else:
                    print("Thank you for playing!")
                    break
                
                      
if __name__ == "__main__":
    main()