# Problem statement
# https://github.com/anomaly2104/lld-parking-lot/blob/master/problem-statment.md
import argparse

from parking import Parking


def slot_allocation(parking_area, slot, registration_number, color):
    parking_area[slot] = {
        "slot": slot,
        "registration_number": registration_number,
        "color": color
    }


def display_allocation(parking_area):
    for slot in parking_area:
        print(f"{slot['slot']} , {slot['registration_number']} , {slot['color']}\n")


NO_OF_COMMANDS = 100


def main():
    index = 0
    while index < NO_OF_COMMANDS:
        command = input()
        tokens = command.split(" ")
        flag = False
        global parking

        if command.startswith('create_parking_lot'):
            # create the parking lot

            if tokens[0] == "create_parking_lot" and (not tokens[1].isalpha()):
                print(f"Created a parking lot with 6 slots")
                no_of_slots = int(tokens[1])
                # print(f"no_of_slots : {no_of_slots}")
                flag = True
                parking = Parking(capacity=no_of_slots, parking_area=[])

        elif command.startswith("park"):
            # park the vehicle

            if tokens[0] == "park":
                registration_no = tokens[1]
                color = tokens[2]
                # print(f"registration_no : {registration_no}")
                # print(f"color : {color}")
                flag = True
                slot = parking.park(
                    registration_number=registration_no,
                    color=color
                )
                if slot == -1:
                    print("Sorry, parking lot is full")
                else:
                    print(f"Allocated slot number: {slot}")

        elif command.startswith("leave"):
            # free you slot
            if tokens[0] == "leave":
                slot_no = int(tokens[1])
                # print(f"slot_no : {slot_no}")
                flag = True
                parking.free_parking_space(
                    slot=slot_no
                )

        elif command.startswith("status"):
            # show the status
            if tokens[0] == "status":
                print(f"Display the status")
                flag = True
                parking.display()

        elif command.startswith("registration_numbers_for_cars_with_colour"):
            # search and display
            if tokens[0] == "registration_numbers_for_cars_with_colour":
                parking.display_with_filter(
                    color=tokens[1],
                    search_key="registration_number"
                )
            flag = True

        elif command.startswith("exit"):
            # stop the application
            print("Stopping")
            break
        else:
            print("Please enter correct command")

        if not flag:
            print(f"Pls check your command")
            print(f"You entered : {command}")

        index = index + 1


if __name__ == "__main__":
    print(f"Parking Lot Running")
    main()
    print(f"Parking Lot Stops")
