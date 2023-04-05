# Vehicle ---> Entry Gate ----> Ticket Generzted ------> Parked at Parking Spot --------> Exit Gate --> Payment and Free Space


# Requirements
# 1. Two types of vehicles
# 2. Return nearest spot
# 3. Multiple entry & exit
# 4. Hourly/ minute based pricing

# 1.
# class ParkingSpot:
# id
# isEmpty
# type
# vehicle
# rate
# parkVehicle(vehicle)
# removeVehicle(vehicle)
# def calculateAmount()
# def isEmpty()

# StrategyDesign => calculation of Amount bases rate & type of vehicle
# TwoWheelerParking implements ParkingSpot
# FourWheelerParking implements ParkingSpot

# ParkingSpot has a vehicle

# class ParkingAreaManager
# ParkingSpotList (has a relationship)
# def initialiseParkingSpotList(ParkingSpotList)
# def findParkingSpace(ParkingSpotList)
# def addParkingSpace(ParkingSpotList)
# def removeParkingSpace(ParkingSpotList)
# def parkVehicle(vehicle)
# def removeVehicle(vehicle)

# TwoWheelerManager implements ParkingAreaManager
# def initialiseParkingSpotList(TwoWheelerParkingSpotList)
#   super().__init(TwoWheelerParkingSpotList)
# FourWheelerManager implements ParkingAreaManager
#   super().__init(FourWheelerParkingSpotList)


# FactoryPattern
# if type == "two-wheeler":
#     ParkingAreaManager = TwoWheelerManager()
# else:
#     ParkingAreaManager = ParkingAreaManager()