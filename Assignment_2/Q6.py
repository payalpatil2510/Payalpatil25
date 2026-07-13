
# W A P to calculat total salary of employee based on basic , da=10% , ta=12%, hrd=15% of basic.
basic = float(input("Enter basic salary:"))
da = 0.10 * basic
ta = 0.12 * basic
hra = 0.15 * basic
total_salary = basic + da + ta + hra
print("Total salary of employee:", total_salary)