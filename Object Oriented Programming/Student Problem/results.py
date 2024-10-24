from dataclasses import dataclass
import random


# Make student class
@dataclass
class pupil:
    Name: str
    Score: int


# Make results list
Results = []

# Loop for all 200 students
for student_number in range(200):
    # Set student name to number
    name = f"Student{str(student_number)}"
    # Set students score to random number 0-100
    score = random.randint(0, 100)
    # Add student to the list of results
    Results.append(pupil(name, score))

# Set highest and second-highest scores to 0
highest_score = 0
second_highest_score = 0

# Loop through all students
for students in Results:
    # If the current student's score is higher than the highest score
    if students.Score >= highest_score:
        # Set the highest score to the current student's score
        highest_score = students.Score
    # If the current student's score is higher than the second-highest score
    elif students.Score > second_highest_score:
        # Set the second-highest score to the current student's score
        second_highest_score = students.Score


# Print the highest score and all students with the score
print(f"Students who achieved the highest score of {highest_score}")
for student in Results:
    if student.Score == highest_score:
        print(student.Name)

# Print empty line
print()

# Print the second-highest score and all students with the score
print(f"Students who achieved the second-highest score of {second_highest_score}")
for student in Results:
    if student.Score == second_highest_score:
        print(student.Name)
