# CLASS METHOD
class Company:
    # Class Variable
    # This variable belongs to the class itself.
    # All objects share this single variable.
    company = "Bansal Towels"

    # Constructor
    def __init__(self, name):
        # Instance Variable
        # Every object has its own copy of this variable.
        self.name = name
    # Class Method
    # It works with the CLASS, not with individual objects.
    @classmethod
    def change_company(cls, new_company): # at place of self we mostly use cls here 
        # Changes the class variable.
        # Since all objects share this variable,
        # the change made in class variables through any 1 objetc
        #is reflected in every object.
        cls.company = new_company
e1 = Company("Shivam")
e2 = Company("Surya")

# Initial Values
print("Before changing company name")
print("-----------------------------")
print("e1 Company :", e1.company)
print("e2 Company :", e2.company)
print("Company.company :", Company.company)
e1.change_company("BTC")

# We could also write:
# Company.change_company("BTC") or e2.change_company()
print("\nAfter changing company name")
print("----------------------------")
print("e1 Company :", e1.company)
print("e2 Company :", e2.company)
print("Company.company :", Company.company)

# -------------------------------
# Instance Variables
# -------------------------------

print("\nEmployee Names")
print("----------------")
print("Employee 1 :", e1.name)
print("Employee 2 :", e2.name)
