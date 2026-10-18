marks1 = float(input("Enter marks for subject 1:"))
marks2 = float(input("Enter marks for subject 2:"))
marks3 = float(input("Enter marks for subject 3:"))
marks4 = float(input("Enter marks for subject 4:"))
marks5 = float(input("Enter marks for subject 5:"))

total = marks1 + marks2 + marks3 + marks4 + marks5
percentage = total/5

print("Total marks:", total)
print("Percentage:", percentage, "%")

if percentage>=90:
    grade = "A+"
elif percentage >=80:
    grade = "A"
elif percentage>=70:
    grade = "B"
elif percentage>=60:
    grade = "C"
else:
    grade = "D"
print("Grade:", grade)