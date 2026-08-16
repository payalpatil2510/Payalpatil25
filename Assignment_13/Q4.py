n = int(input("Enter n: "))

d = {}

for x in range(1, n + 1):
    d[x] = x * x

print("Dictionary:", d)