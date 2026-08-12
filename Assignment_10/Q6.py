lst = [10, 20, 10, 30, 20, 40, 30]

new_list = []

for i in lst:
    found = 0

    for j in new_list:
        if i == j:
            found = 1
            break

    if found == 0:
        new_list = new_list + [i]

print("Original list =", lst)
print("List after removing duplicates =", new_list)