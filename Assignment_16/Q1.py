class Book:
    count = 0

    def __init__(self, bid=0, bname="", price=0, author=""):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

        Book.count = Book.count + 1

    def __del__(self):
        print("Book object destroyed")

    def ShowBook(self):
        print("Book ID     :", self.bid)
        print("Book Name   :", self.bname)
        print("Price       :", self.price)
        print("Author      :", self.author)

    @staticmethod
    def show_count():
        print("Total objects created :", Book.count)
b1 = Book(101, "Python", 500, "John")
b2 = Book()
b1.ShowBook()
print()
b2.ShowBook()
print()
Book.show_count()