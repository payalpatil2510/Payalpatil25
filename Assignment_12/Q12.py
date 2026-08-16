s = input("Enter a string: ")

count = 0

for ch in s:
    if ch >= 'a' and ch <= 'z':
        count = count + 1

print("Number of lowercase characters:", count)