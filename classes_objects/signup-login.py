try:
    createAccount = print("Create Account")
    username = input("Enter Your Username: ")
    email = input("Enter Your Email: ")
    password = input("Enter Your password: ")
    print("User " + username + " " + "created succesfully")
    print("Login to your Account: ")
    login = input("Enter Username: ")
    passConfirm = input("Confirm Your password")
    
    if login == username and passConfirm == password: print("Successfully Logged in")
    else: print("Invalid credentials")


except AttributeError: print("Something went wrong")
finally: print("Login successfull")