lst = [10, 15, 20, 25, 30, 35, 40]

even = []
odd = []

for i in lst:
    if i % 2 == 0:
        even = even + [i]
    else:
        odd = odd + [i]

print("Original list =", lst)
print("Even list =", even)
print("Odd list =", odd)