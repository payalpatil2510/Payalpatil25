

##Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a 3-digit number: "))
d = num // 100
num = num % 10

if d == num:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")