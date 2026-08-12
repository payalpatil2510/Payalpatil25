lst = [1, 2, 3, 4, 5]

cube = []

for i in lst:
    cube = cube + [i * i * i]

print("Original list =", lst)
print("Cube list =", cube)