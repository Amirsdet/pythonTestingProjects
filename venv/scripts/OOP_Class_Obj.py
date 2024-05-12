class Calculator:
    num = 100  # Class var

    def __init__(self, a, b):
        print("I am executing now automaticly ehen the obj is created  ")
        self.fNum = a
        self.SNum = b

    def getData(self):
        print("I am executing as a method ")

    def sum(self):
        return self.fNum + self.SNum+Calculator.num


obj = Calculator(2,3)
# print(obj.getData())
print(obj.sum())

obj1 = Calculator(4,5)
# print(obj1.getData())
print(obj1.sum())

