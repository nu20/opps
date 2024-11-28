class vehicle :
    def __init__(self , max_speed , mileage) :
        self.max_speed = max_speed
        self.mileage = mileage
    def printinfo(self) :
        print("self max_speed :" , self.max_speed)
        print("self mileage :" , self.mileage)
mod = vehicle(240 , 18) 

modx = vehicle(43,54)
modx.printinfo()