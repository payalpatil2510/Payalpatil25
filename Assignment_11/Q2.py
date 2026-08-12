l1 = [10, 30, 20]
l2 = [50, 40, 60]

l3 = l1 + l2

for i in range(len(l3)):
    for j in range(i + 1, len(l3)):
        if l3[i] > l3[j]:
            temp = l3[i]
            l3[i] = l3[j]
            l3[j] = temp

print("Merged and Sorted List:", l3)