
#http://www.w3schools.com/python/python_inheritance.asp
#http://www.w3schools.com/spaces/index.php

class MyClass:
    x = 5
    
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name} ({self.age})"
        
        
p1 = Person('John', 36)
print(p1)