
# 1. Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3
#times.After that program to terminate.

userid = "admin"
password = "1234"

for i in range(3):

    uid = input('Enter UserId:')
    pwd = input('Enter Password:')

    if uid == userid and pwd == password:
        print("Login Successfully")

    else:
        print("Invalid")
        
else:
    print("Program Terminated")
