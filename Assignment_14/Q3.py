words = ["apple", "banana", "apple", "orange", "banana", "apple"]

unique_words = set(words)

for word in unique_words:
    count = words.count(word)
    print(word, ":", count)