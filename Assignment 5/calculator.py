class calculator:
    def getinput(self):
        n1 = int(input('Enter no1:   '))
        n2 = int(input('Enter no2:   '))
        return n1, n2

    def addition(self,num1, num2):
        return num1 + num2
    def subtraction(self,num1, num2):
        return num1 - num2
    def multiplication(self,num1, num2):
        return num1 * num2
    def divison(self,num1, num2):
        return num1 / num2
    
    
obj = calculator()
num1, num2 = obj.getinput()
result = obj.addition(num1, num2)
print("Addition: ",result)
result = obj.subtraction(num1, num2)
print("subtraction: ",result)
result = obj.multiplication(num1, num2)
print("Multiplication: ",result)
result = obj.divison(num1, num2)
print("Divison: ",result)