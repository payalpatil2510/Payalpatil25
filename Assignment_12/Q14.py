s = input("Enter a string: ")

words = s.split()

for i in range(len(words)):
    count = 0

    for j in range(len(words)):
        if words[i] == words[j]:
            count = count + 1

    already = False

    for k in range(i):
        if words[i] == words[k]:
            already = True

    if already == False:
        print(words[i], ":", count)