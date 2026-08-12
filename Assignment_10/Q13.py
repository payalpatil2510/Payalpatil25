lst = [10, 15, 20, 25, 30, 35, 40]

new_list = []

for i in lst:
    if i % 2 != 0:
        new_list = new_list + [i]

print("Original list =", lst)
print("List after removing even numbers =", new_list)