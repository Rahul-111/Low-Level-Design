from parking import Parking


def initialize_parking_lot(no_of_slot):
    parking_obj = Parking(
        capacity=no_of_slot,
        parking_area=[]
    )
    return parking_obj


def read_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        return lines
    # return commands
