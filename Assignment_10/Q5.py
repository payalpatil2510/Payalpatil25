lst = [10, 20, 10, 30, 10, 40]

n = int(input("Enter number: "))

count = 0

for i in lst:
    if i == n:
        count = count + 1

if count > 0:
    print("Element is present")
    print("It is present", count, "times")
else:
    print("Element is not present")