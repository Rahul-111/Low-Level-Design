# class Vehicle:
#     def __init__(self):
#         pass
#
#     def drive(self):
#         print("normal drive capability")
#
#
# class SportsCar(Vehicle):
#     def drive(self):
#         print("special drive capability")
#
#
# class PassengerVehicle(Vehicle):
#     pass
#
#
# class OffloadVehicle(Vehicle):
#     def drive(self):
#         print("special drive capability")


# Problem
# both the sibling[SportsCar, OffloadVehicle] need the same function which is not present in base code , it is duplicated

# Solution create a interface for drive
from abc import ABC, abstractmethod


class DriveStrategy(ABC):
    @abstractmethod
    def drive(self):
        pass


class NormalDriveStrategy(DriveStrategy):
    def drive(self):
        print("normal drive capability")


class SpecialDriveStrategy(DriveStrategy):
    def drive(self):
        print("special drive strategy")


# use of has a relationship

class Vehicle:

    # construction injection
    def __init__(self, driveObject):
        # has a relationship
        self.driveObject = driveObject

    def drive(self):
        self.driveObject.drive()


class OffloadVehicle(Vehicle):

    def __init__(self):
        super().__init__(SpecialDriveStrategy())

    def drive(self):
        print("special drive capability")


d1 = OffloadVehicle()
d1.drive()
