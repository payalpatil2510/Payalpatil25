
n = 5

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    ch = 65
    for j in range(2 * i - 1):
        print(chr(ch), end=" ")
        ch += 1
    print()