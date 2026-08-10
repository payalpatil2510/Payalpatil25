

# 11. WAP to check if a given number is Armstrong number or not. For each task create separate functions.

def armstrong(num):
    temp = num
    total = 0

    digits = len(str(num))

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp = temp // 10

    if total == num:
        return True
    else:
        return False

num = int(input("Enter number: "))

if armstrong(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")