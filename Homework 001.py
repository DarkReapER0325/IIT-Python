name=input("Enter your name here: ")
marks=int(input("Enter the marks of the subject: "))
grade=""

if marks>80:
    grade = "A"
elif marks>=60:
    grade = "B"
elif marks>=40:
    grade = "C"
else:
    grade = "F"
print(name, " " , marks, " ", "You have", grade, "pass")