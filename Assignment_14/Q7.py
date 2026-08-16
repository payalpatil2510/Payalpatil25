set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

missing_in_set2 = set1 - set2
missing_in_set1 = set2 - set1

print("Missing in second set:", missing_in_set2)
print("Missing in first set:", missing_in_set1)