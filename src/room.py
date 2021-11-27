class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.current_num_guests = 0
        self.guests = []
