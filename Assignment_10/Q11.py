lst = [10, 12, 15, 20, 24, 30, 40, 60]

m = int(input("Enter m: "))
n = int(input("Enter n: "))

for i in lst:
    if i % m == 0 and i % n == 0:
        print(i)