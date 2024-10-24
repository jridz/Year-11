def load_array():
    return [
        [60,65,67],
        [65,73,70],
        [72,60,58],
        [85,86,80],
        [68,74,85],
        [58,55,52],
        [70,75,70]
    ]

def print_array(array):
    print("\nAssessment marks:")
    student_num = 1
    for marks in array:
        print(f"Student {student_num}: {marks}")
        student_num += 1

student_marks = load_array()
print_array(student_marks)

