class Book:

    def __init__(self, bid=0, bname="", price=0, author=""):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def __del__(self):
        print("Book object destroyed")

    def ShowBook(self):
        print("Book ID :", self.bid)
        print("Book Name :", self.bname)
        print("Price :", self.price)
        print("Author :", self.author)


b1 = Book()
b1.ShowBook()
print()
b2 = Book(101, "Python Programming", 500, "Guido van Rossum")
b2.ShowBook()