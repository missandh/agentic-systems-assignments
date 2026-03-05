class StudentPerformance:
    def __init__(self, scores):
        """Initialize with a list of scores"""
        self.scores = scores
    
    def score_difference(self):
        """Find the difference between the last score and the first score using indexing"""
        try:
            if len(self.scores) == 0:
                raise ValueError("No scores available to calculate difference")
            
            # Using indexing to get the first and last scores
            first_score = self.scores[0]
            last_score = self.scores[-1]
            difference = last_score - first_score
            print(f"Difference between last and first score is: {difference}")
        except ValueError as e:
            print(e)


# Example usage
if __name__ == "__main__":
    # Take input from user
    user_input = input("Enter scores separated by commas (e.g., 55,65,75,85): ")
    
    try:
        # Convert string input to list of integers
        scores = []
        for score in user_input.split(','):
            scores.append(int(score.strip()))
        student = StudentPerformance(scores)
        student.score_difference()
    except ValueError:
        print("No scores available to calculate difference")
