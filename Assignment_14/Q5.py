words = ["flower", "flow", "flight"]

prefix = ""

for i in range(len(words[0])):
    characters = set()

    for word in words:
        if i < len(word):
            characters.add(word[i])

    if len(characters) == 1:
        prefix = prefix + words[0][i]
    else:
        break

print("Longest common prefix:", prefix)