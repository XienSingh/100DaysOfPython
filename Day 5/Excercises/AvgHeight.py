# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
print(student_heights)
numberOfStudents = 0
totalHeight = 0
for student in student_heights:
    numberOfStudents += 1
    totalHeight += student

print(f"Average Height - {int(totalHeight / numberOfStudents)}")
