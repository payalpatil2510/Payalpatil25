d = {"name": "Payal", "age": 20, "city": "Pune"}

key = input("Enter key to remove: ")

if key in d:
    del d[key]
    print("Dictionary after removing key:", d)
else:
    print("Key does not exist")