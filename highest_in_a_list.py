student_scores = input("Input a list of student scores, separate with a 'space': \n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

sorted_scores = sorted(student_scores)
print(sorted_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")