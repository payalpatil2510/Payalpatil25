
#2. Write a program to check if given number is Armstrong or not using recursive function.

def power(n, p):
    if p == 0:
        return 1
    return n * power(n, p - 1)


def armstrong(n, original, digits):
    if n == 0:
        return 0

    digit = n % 10
    return power(digit, digits) + armstrong(n // 10, original, digits)


num = int(input("Enter a number: "))

digits = len(str(num))

if armstrong(num, num, digits) == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

