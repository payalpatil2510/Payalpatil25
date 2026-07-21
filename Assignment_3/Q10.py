

##Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender = input("Enter Gender (M/F): ")
age = int(input("Enter Age: "))

if (gender == "M" or gender == "m") and age >= 21:
    print("Eligible for Marriage")
elif (gender == "F" or gender == "f") and age >= 18:
    print("Eligible for Marriage")
else:
    print("Not Eligible")