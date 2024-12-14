class calculator:
    def __init__(self,a,b,operation):
        self.a=a
        self.b=b
        self.operation=operation

    def calculate(self):
        if self.operation=="Addition":
            return self.a+self.b
        elif self.operation=="Subtraction":
            return self.a-self.b
        elif self.operation=="Multiplication":
            return self.a*self.b
        elif self.operation=="Division":
            if self.b==0:
                print("Divide by Zero Error")
            else:
                return self.a/self.b
        else:
            print("Invalid Operation")

a=float(input("Enter the value of a :"))
b=float(input("Enter the value of b :"))
operation=input("Enter the type of operation [Addition, Subtraction,Multiplication, Division]")
num=calculator(a,b,operation)
Result=num.calculate()
print(f"The result of {operation} of {a} and {b} is {Result}")