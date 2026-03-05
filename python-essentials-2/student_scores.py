class StudentScores:
    def __init__(self, scores):
        """Initialize with a list of scores"""
        self.scores = scores
    
    def highest_last_two(self):
        """Find the highest score among the last two scores using negative indexing"""
        try:
            if len(self.scores) < 2:
                raise ValueError("Not enough scores to find highest value")
            
            # Using negative indexing to get the last 2 scores
            last_two = self.scores[-2:]
            highest = max(last_two)
            print(f"Highest score among last two is: {highest}")
        except ValueError as e:
            print(e)


# Example usage
if __name__ == "__main__":
    # Take input from user
    user_input = input("Enter scores separated by commas (e.g., 45,67,89,72): ")
    
    try:
        # Convert string input to list of integers
        scores = []
        for score in user_input.split(','):
            scores.append(int(score.strip()))
        student = StudentScores(scores)
        student.highest_last_two()
    except ValueError:
        print("Invalid input. Please enter scores as numbers separated by commas.")
