lst = [1, 2, 3, 4, 5]

square = []
cube = []

for i in lst:
    square = square + [i * i]
    cube = cube + [i * i * i]

print("Number list =", lst)
print("Square list =", square)
print("Cube list =", cube)