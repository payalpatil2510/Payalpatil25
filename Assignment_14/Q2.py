set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

intersection = set1 & set2
set1 = set1 - intersection

print("Set1 after removing intersection:", set1)