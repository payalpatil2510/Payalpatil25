l = [10, 50, 20, 40, 30]

for i in range(len(l)):
    for j in range(0, len(l) - i - 1):
        if l[j] > l[j + 1]:
            temp = l[j]
            l[j] = l[j + 1]
            l[j + 1] = temp

print("Sorted List:", l)
print("Second Largest:", l[-2])