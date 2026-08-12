l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]

intersection = []

for i in l1:
    if i in l2:
        intersection.append(i)

print("Intersection:", intersection)