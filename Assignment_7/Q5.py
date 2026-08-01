
#E.

n = 5

for i in range(1, n + 1):
    if i == 1:
        print(" " * (n - i) * 2 + "1")
    elif i == n:
        for j in range(1, n + 1):
            print(j, end="   ")
        print()
    else:
        print(" " * (n - i) * 2, end="")
        print("1", end="")
        print(" " * (4 * i - 5), end="")
        print(i)