l = ["apple", "hi", "banana", "cat", "elephant"]

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if len(l[i]) > len(l[j]):
            temp = l[i]
            l[i] = l[j]
            l[j] = temp

print("Sorted List:", l)