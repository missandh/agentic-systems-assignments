class StudentMarks:
    def __init__(self, marks):
        """Initialize with a list of marks"""
        self.marks = marks
    
    def last_three_avg(self):
        """Calculate the average of the last 3 marks using negative indexing"""
        try:
            if len(self.marks) < 3:
                raise ValueError("Not enough marks to calculate average")
            
            # Using negative indexing to get the last 3 marks
            last_three = self.marks[-3:]
            average = sum(last_three) / len(last_three)
            print(f"Average of last 3 marks is: {average}")
        except ValueError as e:
            print(e)


# Example usage
if __name__ == "__main__":
    # Take input from user
    user_input = input("Enter marks separated by commas (e.g., 50,60,70,80,90): ")
    
    try:
        # Convert string input to list of integers
        marks = []
        for mark in user_input.split(','):
            marks.append(int(mark.strip()))
        student = StudentMarks(marks)
        student.last_three_avg()
    except ValueError:
        print("Invalid input. Please enter marks as numbers separated by commas.")
