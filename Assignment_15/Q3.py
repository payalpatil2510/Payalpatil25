class Shirt:

    def __init__(self, sid=0, sname="", type="", price=0, size=""):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def __del__(self):
        print("Shirt object destroyed")

    def ShowBook(self):
        print("Shirt ID :", self.sid)
        print("Shirt Name :", self.sname)
        print("Type :", self.type)
        print("Price :", self.price)
        print("Size :", self.size)


s1 = Shirt()
s1.ShowBook()
print()
s2 = Shirt(101, "Formal Shirt", "Formal", 1200, "Large")
s2.ShowBook()