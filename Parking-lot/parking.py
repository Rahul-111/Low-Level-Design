class Parking:

    def __init__(
            self,
            capacity: int,
            parking_area: list
    ) -> None:
        self.capacity = capacity
        # create list of given size
        self.parking_area = ["empty"] * capacity

    def park(self, registration_number, color):

        # find the slot bases parking criteria
        free_slot = self.find_slot()
        if free_slot == -1:
            return -1
        # update the parking
        self.parking_area[free_slot] = {
            "slot": free_slot,
            "registration_number": registration_number,
            "color": color
        }
        return free_slot

    def find_slot(self):
        # iterate the list and find free slot nearest
        for index, slot in enumerate(self.parking_area):
            # print(f"index : {index} , slot : {slot}")
            if slot == "empty":
                return index

        return -1

    def display(self):
        print(f"Slot No,    Registration No,    Color")
        for lot in self.parking_area:
            if lot != "empty":
                print(f"{lot['slot']}\t\t{lot['registration_number']}\t\t{lot['color']}")

    def free_parking_space(self, slot):
        if slot < self.capacity:
            self.parking_area[slot] = "empty"
            print(f"Slot number {slot} is free")
        else:
            print(f"Please check the Input")

    def display_with_filter(self, filter_by, color=None, search_key=None):
        # loop over array and find car
        result = []
        for slot in self.parking_area:
            if slot != "empty":
                if filter_by.lower() == "color":
                    if slot['color'] == color:
                        result.append(slot)
                elif filter_by.lower() == "registration_number":
                    if slot['registration_number'] == search_key:
                        result.append(slot)

        if result:
            print(f"Slot No,    Registration No,    Color")
            for index, slot in enumerate(result):
                if slot != "empty":
                    print(f"{slot['slot']}\t\t{slot['registration_number']}\t\t{slot['color']}")

        else:
            print(f"Not Found")


