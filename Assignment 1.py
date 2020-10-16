'''
EDUCATION OOP

- SCHOOL DETAILS tick
- CHILD DETAILS
- GRADES

'''

class School():
    def __init__(self, schoolName, location):
        self.schoolName = schoolName
        self.location = location
        print('(Initialized School Class: {})'.format(self.schoolName))
        print('(Initialized School Class: {})'.format(self.location))

    def getSchoolName(self):
        return self.schoolName

    def getSchoolLocation(self):
        return self.location

    
    def __str__(self):
        return f"School Name: {self.schoolName}. School Location: {self.location}"
    
    def __repr__(self):
        return f"{self.schoolName!r}, {self.location!r}"
  
print(repr(School))


    #Edu = School("Royal Grammar School",
               #"Newcastle Upon Tyne- Jesmond")

    #print(Edu)
    #print(repr(School))


    #2nd class about the child attending the School
class Child(School):
    def __init__(self, name, age, yeargroup, schoolName, location):
        self.name = name
        self.age = age
        self.yeargroup = yeargroup
        super().__init__(schoolName, location)

        #super().__init__(schoolName, location)
        print('(Initialized Child Class: {})'.format(self.name))
        print('(Initialized Child Class: {})'.format(self.age))
        print('(Initialized Child Class: {})'.format(self.yeargroup))
        print()
        print(self.name + "'s item's '")
        print()
        

        #School.__init__(self, schoolName, location)

    # Access from inherited class where the child goes to School
      #  super().__init__(schoolName, location)
    
    #Access composition class
      #self.obj_overview = Overview(attendance, grade)
    
    def getChildName(self):
        return self.name

    def getChildAge(self):
        return self.age

    def getChildYearGroup(self):
        return self.yeargroup
 #this string is displaying the information
    #def __str__(self):
      #return f"{self.name} is {self.age} and is currently is yearx  {self.yeargroup} and the school name is {self.location } {super().__str__()}"

#Kieran = Child("Kieran", 12, 12, "ROYAL GRAMMAR SCHOOL", "Newcastle Upon Tyne")
#print(Kieran)

 # currently this does nothing, how can i get this into the program?
class Overview(Child, School):
    def __init__(self, attendance, grade, name, age, yeargroup, schoolName, location):
        self.attendance = attendance
        self.grade = grade
        super().__init__(name, age, yeargroup, schoolName, location)
        #print('(Initialized Overview Class: {})'.format(self.name))

    def getAttendance(self):
        return self.attendance

    def getGrade(self):
        return self.grade
    
    # inherited
    # __Str__ informal representation
    def __str__(self):
        return f"{self.name}s attendance has been oustanding, acheiving an overall attendance of: {self.attendance}. He is currently Aged: {self.age} and is in YearGroup:  {self.yeargroup} and his overall grade for the year is: {self.grade} - he attends the school in {self.location} and the name of the school is {self.schoolName}"

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__dict__}"
       
        
        
#{super().__str__()}"


#prints a blank line
print()
# this one accepts the data to be passed 
#person 1
p1 = Overview(80, "A", "kieran", 8, 12, "Royal Grammar School", "Newcastle Upon Tyne")
print(p1)
#p1.schoolName = "ResourceWarning"
print()
p2 = Overview(20, "B", "Paj", 31, "University", "Sunderland University", "Sunderland")
print(p2)
print()

#access repr string
print()
print("Testing the REPR")
print()
print(repr(p1))
#print(p1.getSchoolName())

#p1.name = "alan"
#p1.age = "12"
#p1.yeargroup = 8
#p1.location = "nEWCASTLE"

#print()
#print(Overview.__bases__)
 #returns a list of all the members in the specified obkect
#print(dir(p1))


#person 2
#p2 = Overview(10, 12, "james", 1, 5, "england", "stella")
#print(Overview)