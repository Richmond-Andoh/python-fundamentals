# class myClass:
#     x = 3
# clasd1 = myClass()
# print(clasd1.x)

try:
    class Person:
        def __init__(self, name, age, gender):
            self.name = name
            self.age = age
            self.gender = gender
            
    # person1 = Person("John", int(23), "Male")
    # print(person1.name)
    # print(type(person1.age))

    #turning this into user input
    '''
    name = input("Enter Your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter Your gender: ")

    print(person1.name)
    print(person1.age)
    print(person1.gender)
    '''
    person1 = Person("John", int(20), "Male")
    del person1.name
    print(person1.name)
except AttributeError: print("Somethong went wrong")
finally: print("Name was deleted successfuly")
