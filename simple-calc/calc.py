num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
opp = input("Enter operator: ")

if opp == "+":
    print(num1 + num2)
elif opp == "-":
    print(abs(num1 - num2))
elif opp == "/":
    print(round(num1 / num2))
elif opp == "*": 
    print("Their multiplication is " + " " + num1 * num2)
else: print("Invalid operator")