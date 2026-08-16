numbers = [2, 5, 3, 8, 1, 7]

number_set = set(numbers)

max_product = 0
pair = ()

for x in number_set:
    for y in number_set:
        if x != y:
            product = x * y

            if product > max_product:
                max_product = product
                pair = (x, y)

print("Numbers:", pair)
print("Maximum product:", max_product)