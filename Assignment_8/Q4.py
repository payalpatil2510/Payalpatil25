
# 4. Sum of all odd numbers between 1 to n

def odd_sum(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i
    return total

n = int(input("Enter n: "))

print("Sum of Odd Numbers =", odd_sum(n))