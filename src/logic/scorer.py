class Scorer:
    """Updates and retrieves the user's score based on penalties for incorrect guesses. 
    """
    def __init__(self, initial_score=100):
        self.score = initial_score
    def update_score(self, penalty=10):
        self.score -= penalty
        self.score = max(0, self.score)     
    def get_score(self)-> int:
        return self.score