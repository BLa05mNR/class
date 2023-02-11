class Math:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b
    
    def subtraction(self):
        return self.a - self.b
    
    def multiplication(self):
        return self.a * self.b
        
    def division(self):
        return self.a / self.b
        
math_object = Math(3,9)
print("addition", math_object.addition())
print("subtraction", math_object.subtraction())
print("multiplication", math_object.multiplication())
print("division", math_object.division())