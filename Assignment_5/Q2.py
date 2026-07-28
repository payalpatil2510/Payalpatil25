

# 2.Enter number of students from user. For those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and
#average percentage of students.

n = int(input("Enter number of student:"))
total_per = 0

for i in range(n):
    total = 0
    print("Student", i +1)
    
for j in range(5):
    marks = int(input("Enter marks: "))
    total = total + marks

    per = total / 5
    print("Percentage =", per)

    total_per = total_per + per

print("Average Percentage =", total_per / n)