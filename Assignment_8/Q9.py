

# 9. Write a program to check if entered number is a palindrome or not

def reverse_number(num):
    rev = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10

    return rev

num = int(input("Enter number: "))

if num == reverse_number(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")