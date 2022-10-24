def execute_command(parking, input_command):
    flag = False

    if input_command[0] == "park":
        registration_no = input_command[1]
        color = input_command[2]
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

    elif input_command[0] == "leave":
        # free you slot
        slot_no = int(input_command[1])
        # print(f"slot_no : {slot_no}")
        flag = True
        parking.free_parking_space(
            slot=slot_no
        )

    elif input_command[0] == "status":
        print(f"Display the status")
        flag = True
        parking.display()

    elif input_command[0] in [
        "registration_numbers_for_cars_with_colour",
        "slot_numbers_for_cars_with_colour"
    ]:
        # search and display
        parking.display_with_filter(
            filter_by="color",
            color=input_command[1],
            search_key="registration_number"
        )
        flag = True
    elif input_command[0] == "slot_number_for_registration_number":
        # search and display
        registration_number = input_command[1]
        parking.display_with_filter(
            filter_by="registration_number",
            search_key=registration_number
        )
        flag = True

    elif input_command[0] == "exit":
        # stop the application
        print("Stopping")
        return -1

    else:
        print("Please enter correct command")

    if not flag:
        print(f"Pls check your command")
        print(f"You entered : {input_command}")

    return 1
