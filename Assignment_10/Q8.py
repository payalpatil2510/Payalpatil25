lst = [10, 20, 30, 40]

new_list = []

for i in lst:
    new_list = new_list + [i]

print("Original list =", lst)
print("Duplicate list =", new_list)

print(lst is new_list)