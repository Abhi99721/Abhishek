class python:

     def __init__(self):              # constructor
         self.x = 0
         self.y = 0

     def getinput(self):                            # instance method
         self.x = int(input('Enter x:   '))
         self.y = int(input('Enter y:   '))
         self.z = int(input('Enter z:   '))

     def sqsum(self):
         return (self.x * self.x) + (self.y * self.y) + (self.z * self.z)

obj = python()                      # calling construtor
obj.getinput()
res = obj.sqsum()
print("Squared values : ",res)