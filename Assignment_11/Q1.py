l = [10, 15, 20, 25, 30, 35]

even = []
odd = []

for i in l:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even List:", even)
print("Odd List:", odd)