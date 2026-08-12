lst = [10, 20, 10, 30, 10, 40, 10]

n = int(input("Enter element to remove: "))

new_list = []

for i in lst:
    if i != n:
        new_list = new_list + [i]

print("List after removing element =", new_list)