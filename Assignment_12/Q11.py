s = input("Enter a string: ")

new = ""

for ch in s:
    if ch == ' ':
        new = new + '-'
    else:
        new = new + ch

print("New string:", new)