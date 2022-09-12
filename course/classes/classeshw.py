"""
Tristan Shawn Den Ouden 7/8/2021

Homework #9: Classes
"""

class Vehicle():
    #Initialise
    def __init__(self,Make,Model,Year,Weight,NeedsMaintenance,TripsSinceMaintenance):
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Weight = Weight
        self.NeedsMaintenance = NeedsMaintenance
        self.TripsSinceMaintenance = TripsSinceMaintenance

    #Set attributes of the car
    def setMake(self,newMake):
        self.Make = newMake
    def setModel(self,newModel):
        self.Model = newModel
    def setYear(self,newYear):
        self.Year = newYear
    def setWeight(self,newWeight):
        self.Weight = newWeight

#Inherits the Vehicle class
class Cars(Vehicle):
    #Initialise Cars
    def __init__(self,Make,Model,Year,Weight,NeedsMaintenance=False,TripsSinceMaintenance=0,isDriving=False):
        #Initialise the Parent Class
        Vehicle.__init__(self,Make,Model,Year,Weight,NeedsMaintenance,TripsSinceMaintenance)
        self.isDriving = isDriving
    
    #Start driving method
    def startDriving(self):
        self.isDriving = True

    #Stop driving method, increments Trips Since Maintenance, Checks for maintenance
    def stopDriving(self):
        self.isDriving = False
        self.TripsSinceMaintenance += 1
        if self.TripsSinceMaintenance > 100:
            print(self.Make,self.Model, " needs maintenace!")
            self.NeedsMaintenance = True
            self.repairCar()
    
    #Repairs car method, resets Trips Since Maintenance
    def repairCar(self):
        if self.NeedsMaintenance == True:
            self.TripsSinceMaintenance = 0
            print(self.Make,self.Model, " has been repaired.")
            self.NeedsMaintenance = False

    #Drives a car for X amount of trips, using startDriving() and stopDriving() methods
    def carTrip(self,trips):
        #Adds 1 because the counter goes up to, but including
        #E.g (100) = 99 but +1 makes it 100 trips
        trips += 1
        for counter in range(trips):
            self.startDriving()
            self.stopDriving()


#Examples
car1 = Cars("Ford",6,2020,1300)
car2 = Cars("Nissan",3,2021,1450)
car3 = Cars("Toyota",5,2020,1200)

#Trips
car1.carTrip(50)
car2.carTrip(100)
car3.carTrip(200)

#Extra Credit
class Planes(Vehicle):
    #Initialise
    def __init__(self,Make,Model,Year,Weight,NeedsMaintenance=False,TripsSinceMaintenance=0, isFlying=False):
        Vehicle.__init__(self,Make,Model,Year,Weight,NeedsMaintenance,TripsSinceMaintenance)
        self.isFlying = isFlying
    
    #startFlying() method, starts flight or rejects flight if plane needs maintenance
    def startFlying(self):
        if self.NeedsMaintenance == False:
            self.isFlying = True
        else:
            return False
    
    #stopFlying() method, checks if plane needs maintenance
    def stopFlying(self):
        self.isFlying = False
        self.TripsSinceMaintenance += 1
        if self.TripsSinceMaintenance > 100:
            print(self.Make,self.Model, " needs maintenace!")
            self.NeedsMaintenance = True

    #The plane takes X amount of flights, using startFlying() and stop Flying() methods
    def Flights(self,flights):
        #Adds 1 because the counter goes up to, but including
        #E.g (100) = 99 but +1 makes it 100 trips
        flights += 1
        for counter in range(flights):
            self.startFlying()
            self.stopFlying()
            #Error prompt, rejects flight
            if self.NeedsMaintenance == True:
                print("Can't fly until the plane has been repaired.")
                break

#Examples
Plane1 = Planes("Sky Airlines",68,2019,44700)
Plane2 = Planes("Flight Airlines",72,2020,45000)
Plane3 = Planes("Fast Airlines",334,2017,48900)

#Flights
Plane1.Flights(50)
Plane2.Flights(100)
Plane3.Flights(200)