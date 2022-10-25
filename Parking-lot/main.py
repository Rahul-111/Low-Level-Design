# Problem statement
# https://github.com/anomaly2104/lld-parking-lot/blob/master/problem-statment.md
import argparse
from execute_commands import execute_command
from utils import read_file, initialize_parking_lot

NO_OF_COMMANDS = 100

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_mode", type=str, help="file or cmd")
    argv = vars(parser.parse_args())
    mode = argv["input_mode"]
    global parking

    if mode == "file":
        # read commands from the file
        print(f"Parking Lot Running")
        commands = read_file('input_file.txt')
        for command in commands:
            command = command.replace('\n', "").split(" ")
            if command[0] == "create_parking_lot":
                # add check for input type should be integer
                parking = initialize_parking_lot(
                    no_of_slot=int(command[1])
                )
                continue

            result = execute_command(
                parking=parking,
                input_command=command
            )

            if result == -1:
                break

    elif mode == "cmd":
        # start reading the input from the console itself
        print(f"Parking Lot Running")
        while True:
            command = input()
            if command == "exit":
                break

            command = command.split(" ")
            if command[0] == "create_parking_lot":
                # initialize parking area
                parking = initialize_parking_lot(
                    no_of_slot=int(command[1])
                )
                continue

            result = execute_command(
                parking=parking,
                input_command=command
            )

            if result == -1:
                break

    else:
        print(f"You entered wrong input , You entered : {mode}")

    print(f"Parking Lot Stops")
