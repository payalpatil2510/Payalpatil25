class Distance:
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm
    def __add__(self, other):

        km = self.km + other.km
        m = self.m + other.m
        cm = self.cm + other.cm
        if cm >= 100:
            m = m + cm // 100
            cm = cm % 100
        if m >= 1000:
            km = km + m // 1000
            m = m % 1000
        return Distance(km, m, cm)
    def __sub__(self, other):
        d1 = self.km * 100000 + self.m * 100 + self.cm
        d2 = other.km * 100000 + other.m * 100 + other.cm
        diff = d1 - d2
        km = diff // 100000
        diff = diff % 100000

        m = diff // 100
        cm = diff % 100

        return Distance(km, m, cm)

    def display(self):
        print(self.km, "km", self.m, "m", self.cm, "cm")

    def __del__(self):
        print("Object destroyed")
d1 = Distance(5, 600, 50)
d2 = Distance(2, 500, 75)
print("First Distance:")
d1.display()
print("Second Distance:")
d2.display()
d3 = d1 + d2
print("Addition:")
d3.display()
d4 = d1 - d2
print("Subtraction:")
d4.display()