'''
MSc Computer Systems and Management
CSTM65 Software Engineering Principles
Author: Paul Jones
Date: 12/10/2020
'''


class River(): #Defines a class in python, in this case the class is called 'River'

    Canoeing = "Yes" # this is a class vriable.  Every instance of the River class will have this attribute

    def __init__(self, RiverName, Location, Fishing): # This initialises the class to have initial values of RiverName and Location
        self.RiverName = RiverName #sets the attributes for each instance of the class
        self.Location = Location #sets the attributes for each instance of the class
        self.Fishing = Fishing #sets the attributes for each instance of the class

    def FishingIssue(self):
        if self.Fishing == True:
            return f"{self.RiverName} has fishing so be wary of fishermen"
        else:
            return f"{self.RiverName} has no fishing so have fun!"
    
    def __str__(self):
        return f"River Name: {self.RiverName}. Location: {self.Location}"

    def __repr__(self):
        return "River()"
        
print()

class RiverDetails(River):

    def __init__(self, RiverLength, Grade):
        self.RiverLength = RiverLength
        self.Grade = Grade
        super().__init__(RiverName, Location, Fishing)


    def Rating(self):
        if self.Grade > 3:
            return f"{self.RiverName} is rated Extreme"
        elif self.Grade == 3:
            return f"{self.RiverName} is rated HARD!"
        elif self.Grade < 3:
            return f"{self.RiverName} is rated Easy!"
        

    def __str__(self):
        return f"River Name: {self.RiverName}. Location: {self.Location}"

    def __repr__(self):
        return "RiverDetails()"


class Rapids(River, RiverDetails):
    pass




'''
Spey = River("River Spey", "Scotland", True)
Wye = River("River Wye", "Wales", False)
Tees = River("River Tees", "NE England", False)
Thames = River ("River Thames", "SE England", True)

print(repr(Spey))
print(str(Spey))
'''
