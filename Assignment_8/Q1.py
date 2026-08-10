
# 1.Write a program to calculate area of rectangle

def area_rectangle(length, width):
    return length * width

l = float(input("Enter length: "))
w = float(input("Enter width: "))

print("Area of Rectangle =", area_rectangle(l, w))