class Shirt:
    size_price = {
        "small": 0,
        "medium": 10,
        "large": 20,
        "xlarge": 30}

    def __init__(self, sid=0, sname="", type="", price=0, size="small"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def __del__(self):
        print("Shirt object destroyed")

    def ShowShirt(self):
        print("Shirt ID     :", self.sid)
        print("Shirt Name   :", self.sname)
        print("Type         :", self.type)
        print("Original Price:", self.price)
        print("Size         :", self.size)
        print("Final Price  :", self.get_price())

    @staticmethod
    def calculate_price(price, size):
        if size == "small":
            return price
        elif size == "medium":
            return price + (price * 10 / 100)
        elif size == "large":
            return price + (price * 20 / 100)
        elif size == "xlarge":
            return price + (price * 30 / 100)
        else:
            return price
    def get_price(self):
        return Shirt.calculate_price(self.price, self.size)

s1 = Shirt(101, "Formal Shirt", "Formal", 1000, "small")
s2 = Shirt(102, "Formal Shirt", "Formal", 1000, "medium")
s3 = Shirt(103, "Formal Shirt", "Formal", 1000, "large")
s4 = Shirt(104, "Formal Shirt", "Formal", 1000, "xlarge")
s1.ShowShirt()
print()
s2.ShowShirt()
print()
s3.ShowShirt()
print()
s4.ShowShirt()