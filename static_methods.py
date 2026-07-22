# Static methods are those methods ehich are are shared by all the object of
# a class means they are of class and called by the class name also
# they don't have any self argumnet

class addition:
    c=10
    @staticmethod  # keyword to create static method
    def add(a,b):
        print(f"{a} + {b} = {a+b}")
addition.add(12,1) # calling static method by using class name
h = addition() # creating object of addition class
h.add(12,11)

