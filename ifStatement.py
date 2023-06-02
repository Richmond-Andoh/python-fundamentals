def sum_function(x, y):
    return x + y

x = int(input("Enter any value for x: "))
y = int(input("Enter any value for y: "))

if x <= 0 and y <= 0:
    print("Both x and y must postive values")
elif x > 0 and y > 0 and x != y:
    print(f"The sum of x and y is {sum_function(x, y)}")
elif x == y:
    print(f"The values are equal and so their sum {sum_function(x, y)} is also accepted")
else:
    print("We don't accept the sum of two negative values")
