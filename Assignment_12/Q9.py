s = input("Enter a string: ")

characters = 0
words = 0

for ch in s:
    characters = characters + 1

    if ch == ' ':
        words = words + 1

if characters > 0:
    words = words + 1

print("Number of characters:", characters)
print("Number of words:", words)