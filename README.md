# FindMyGuess
A simple number guessing game where the computer selects a random number between 1 and 100, and the player tries to guess it. After each incorrect guess, the player receives hints to help them get closer to the correct number. The game continues until the player guesses the correct number. For every incorrect guess, the player's score decreases by 10 point, starting from a maximum score of 100 points.
## How to Play
1. Run the main script.
2. Enter your guess when prompted.
3. Receive hints if your guess is incorrect.
4. Continue guessing until you find the correct number.
5. After guessing correctly, you can choose to play again or exit the game.
## Requirements
- Python 3.6 or higher
## Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:sanazaadel/FindMyGuess.git
   ```
2. Navigate to the project directory:
   ```bash
   cd FindMyGuess
   ```
3. Install any required dependencies (if applicable):
   ```bash
   pip install -r requirements.txt
   ```
## Running the Game
Before running the main script, ensure that the `PYTHONPATH` environment variable includes the project directory. You can set it using the following command:
```bash
export PYTHONPATH=$PYTHONPATH:{pwd}
```
To start the game, run the following command in your terminal:
```bash
python src/main.py
```
## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.                                                      