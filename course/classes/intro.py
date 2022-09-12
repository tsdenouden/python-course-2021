
#Introduction to classes
"""
#Class - an object with attributes
class ClassName:
    #Initialiser function
    def __init__(self):
        #Attribute belongs to the class
        self.Attribute = 0
    
    def AnotherFunction(self):
        #Action(s)
"""

class Team:

    #Intialiser function
    #Requires 3 inputs
    #If there is no input, the placeholder values are used
    #E.g Name = "Name"
    def __init__(self,Name="Name",Origin="Origin"):
        self.TeamName = Name
        self.TeamOrigin = Origin
    
    def DefineTeamName(self,Name):
        self.TeamName = Name

    def DefineTeamOrigin(self,Origin):
        self.TeamOrigin = Origin

"""
class InheritanceClassName(ParentClass):
    def __init__(self,Input1,Input2):
        ParentClass.__init__(self)
        self.Attribute1 = Input1
        self.Attribute2 = Input2
        self.Attribute3 = 0

    def AnotherMethod(self):
        print("boom")
        #Action(s)
"""

class Player(Team):
    def __init__(self):
        Team.__init__(self)
        self.PlayerName = "None"
        self.PlayerPoints = 0
    
    def ScoredPoint(self):
        self.PlayerPoints += 1
    
    def setName(self,Name):
        self.PlayerName = Name

Player1 = Player()

print(Player1.PlayerName)
print(Player1.PlayerPoints)
Player1.DefineTeamName("Sharks")
print(Player1.TeamName)
print(Player1.TeamOrigin)

"""
#Assign this class to this variable
Team1 = Team("Tigers","Chicago")
print(Team1.TeamName)

#Dont need to type self here
Team1.DefineTeamName("Dolphins")
print(Team1.TeamName)

#
Team1.DefineTeamOrigin("Chicago")
print(Team1.TeamOrigin)


"""

"""
class Team:

    #Function inside class = method
    def __init__(self,Name,Origin):
        self.TeamName = "Name"
        self.TeamOrigin = "Origin"

Team1 = Team("Tigers","Chicago")
print(Team1.TeamName)
"""



"""


Team2 = Team("Hawks","New York")

print(Team2.TeamName)
print(Team2.TeamOrigin)

"""