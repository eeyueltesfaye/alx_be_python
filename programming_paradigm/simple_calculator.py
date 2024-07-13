# simple_calculator.py

class SimpleCalculator:
    

    def add(self, a, b):
       return a + b

    def subtract(self, a, b):
       return a - b

    def multiply(self, a, b):
       return a * b

    def divide(self, a, b):
   
        if b == 0:
            return None
        return a / b
    
p1 = SimpleCalculator().divide(3,0)
print(p1)