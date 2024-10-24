mark = int(input("Student mark: "))
if mark >=90:
    grade = "A"
elif mark >=75:
    grade = "B"
elif mark >=60:
    grade = "C"
elif mark >=40:
    grade = "D"
elif mark <40:
    grade = "E"
else:
    grade = "Invalid Entry"
print("Student receved a" + "\033[1;31m " + grade)