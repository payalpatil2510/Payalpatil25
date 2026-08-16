d1 = {"a": 10, "b": 20}
d2 = {"c": 30, "d": 40}

d3 = d1.copy()

for key in d2:
    d3[key] = d2[key]

print("Combined Dictionary:", d3)