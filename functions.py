#functions definition
def greetings_fun(*names):
    print("Hello" + " " + names[2] + " You are welcome to python tutorials")

greetings_fun("Richmond", "John", "Kofi", "Bismark")

#taking input from user
def userInfo(name, email):
    print("Hello" + " " + name + " " + "Your generated email is" + " " + email)

name = input("Enter Your name: ")
email = input("Enter Your email: ")
userInfo(name, email)