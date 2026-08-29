class Product:
    discount = 10

    def __init__(self, pid=0, pname="", price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def __del__(self):
        print("Product object destroyed")

    def ShowProduct(self):
        print("Product ID   :", self.pid)
        print("Product Name :", self.pname)
        print("Price        :", self.price)
        print("Quantity     :", self.quantity)
    @staticmethod
    def apply_discount(price):
        discount_amount = price * Product.discount / 100
        final_price = price - discount_amount
        return final_price
p1 = Product(101, "Laptop", 50000, 2)
p2 = Product()
p1.ShowProduct()
print("Discount     :", Product.discount, "%")
print("Final Price  :", Product.apply_discount(p1.price))
print()
p2.ShowProduct()