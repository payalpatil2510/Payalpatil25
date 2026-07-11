
#Write a program to enter P,T,R and Tcalculate compound interest.
P = float(input('Enter the principal amount:'))
T = float(input('Enter the time in years:'))
R = float (input('Enter the rate of intrest:'))
CI = P * (pow((1+R/100),T))
print('The compound intrest is:',CI)
