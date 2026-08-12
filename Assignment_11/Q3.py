l = [[1, 5], [2, 3], [3, 4], [4, 1]]

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i][1] > l[j][1]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp

print("Sorted List:", l)