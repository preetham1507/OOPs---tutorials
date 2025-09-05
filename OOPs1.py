#How do we initiate a Class

class Employee:
    # Special Method - Constructor
    def __init__(self):
        self.name = "Preetham"
        self.id =15
        self.designation = "Analyst" 
        print("Attributes have been initiated")

    # Methods
    def travel(self,destination):
        print(f"travelling to {destination}")


sam = Employee()
print(sam.designation)
sam.travel("Kerala")