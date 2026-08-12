l = [10, 15, 20, 25, 30, 35, 40]

new_list = []

for i in l:
    if i % 2 != 0:
        new_list.append(i)

print("List after removing even numbers:", new_list)