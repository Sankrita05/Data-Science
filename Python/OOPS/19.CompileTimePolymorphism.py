class MyClass:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

# This will result in an error in Python

def add(a, b, c=None):
    if(c):
        return a+b+c 
    else:
        return a+b 

print(add(10, 12))