# classes are user defined blueprint or prototype
# methods, class variable, instance variable constructor
# self keyword is mandatory for calling variables into method
# instance and class variables have different purpose
# constructor name should be __init__
# new keyword is not required while creating the object

def getData():
    print("I am in getData method")


class Calculator:
    num = 100  # Class variable

    # default constructor
    def __init__(self, a, b):
        self.FirstNumber = a
        self.SecondNumber = b
        print("Default constructor")

    def summation(self):
        return self.FirstNumber + self.SecondNumber + Calculator.num


obj = Calculator(2, 3)  # Syntax to create object
# obj.getData()  # syntax to call method
print(obj.summation())  # Syntax to access variable in method

obj1 = Calculator(4, 5)  # Syntax to create object
# obj1.getData()  # syntax to call method
print(obj1.summation())  # Syntax to access variable in method
