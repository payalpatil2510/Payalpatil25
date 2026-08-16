d = {"name": "Payal", "age": 20, "city": "Pune"}

key = input("Enter key to search: ")

if key in d:
    print("Key exists in dictionary")
else:
    print("Key does not exist in dictionary")