
#write a program to reverse three digit number.

num = int(input("Enter a three-digit number: "))
digit1 = num % 10
digit2 = (num // 10) % 10
digit3 = num // 100
reverse = digit1 * 100 + digit2 * 10 + digit3
print("Reverse number is", reverse)
