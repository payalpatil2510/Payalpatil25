
#10. Write a program to reverse a number using recursion.

def reverse(n, rev=0):
    if n == 0:
        return rev

    rev = rev * 10 + n % 10

    return reverse(n // 10, rev)


n = int(input("Enter a number: "))

print("Reverse =", reverse(n))