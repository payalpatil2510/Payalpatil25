lst = [10, 20, 30, 40, 50]

rev = []

i = len(lst) - 1

while i >= 0:
    rev = rev + [lst[i]]
    i = i - 1

print("Original list =", lst)
print("Reversed list =", rev)