class Product:

    def __init__(self, pid=0, pname="", price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def __del__(self):
        print("Product object destroyed")

    def ShowBook(self):
        print("Product ID :", self.pid)
        print("Product Name :", self.pname)
        print("Price :", self.price)
        print("Quantity :", self.quantity)

p1 = Product()
p1.ShowBook()
print()
p2 = Product(101, "Laptop", 50000, 2)
p2.ShowBook()