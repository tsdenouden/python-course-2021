


class Pet:
    def __init__(self,n,a,h,p):
        self.name = n
        self.age = a
        self.hunger = h
        self.playful = p
    
    #getters

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getHunger(self):
        return self.hunger

    def getPlayful(self):
        return self.playful

    #setters
    def setName(self,xname):
        self.name = xname
    
    def setAge(self,xage):
        self.age = xage
    
    def setHunger(self,xhunger):
        self.hunger = xhunger
    
    def setPlayful(self,xplayful):
        self.playful = xplayful

    def __str__(self):
        return(self.name + " is " + str(self.age) + " years old")


class Dog(Pet):
    def __init__(self,name,age,hunger,playful,breed,FavoriteToy):
        Pet.__init__(self,name,age,hunger,playful)
        self.breed = breed
        self.FavoriteToy = FavoriteToy 

    def wantsToPlay(self):
        if self.playful == True:
            return ("The dog wants to play with " + self.FavoriteToy)
        else:
            return ("The dog doesn't want to play")


class Cat(Pet):
    def __init__(self,name,age,hunger,playful,place):
        Pet.__init__(self,name,age,hunger,playful)
        self.FavoritePlaceToSit = place

    def wantsToSit(self):
        if self.playful == False:
            return ("Cat wants to sit in",self.FavoritePlaceToSit)
        else:
            return ("The cat wants to play")
    
    def __str__(self):
        return(self.name + "likes to sit in " + self.FavoritePlaceToSit)


class Human:
    def __init__(self,name,Pets):
        self.name = name
        self.Pets = Pets

    def hasPets(self):
        if len(self.Pets) != 0:
            return ("Yes")
        else:
            return ("No")
        



#Dog
huskyDog = Dog("Snowball",5,False,True,"Husky","Stick")

Play = huskyDog.wantsToPlay()

print(Play)

huskyDog.playful = False

Play = huskyDog.wantsToPlay()

print(Play)


#Cat
typicalCat = Cat("Fluffy",3,False,False,"the sun ray")

Sit = typicalCat.wantsToSit()

print(Sit)



#Human
yourAverageHuman = Human("Alice",[huskyDog,typicalCat])

hasPet = yourAverageHuman.hasPets()

print(hasPet)

