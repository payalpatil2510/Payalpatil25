
#Write a program to prompt user to enter userid and password. After verifying
#userid and password display a 4 digit random number and ask user to enter the
#same. If user enters the same number then show him success message otherwise
#failed. (Something like captcha)


userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == "admin" and password == "1234":

    user = int(input("Enter the captcha: "))

    
       