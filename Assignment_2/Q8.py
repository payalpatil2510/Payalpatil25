
#write a program to swap two numbers using third variable.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Before swapping:")
print("a =", a)
print("b =", b)
temp = a
a = b
b = temp
print("After swapping:")
print("a =", a)
print("b =", b)