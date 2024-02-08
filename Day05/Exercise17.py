# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇

high_score = student_scores[0]

for number in student_scores[1:]:
    if number > high_score:
        high_score = number
print(f"The highest score in the class is: {high_score}")