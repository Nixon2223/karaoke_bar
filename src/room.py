class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.current_num_guests = 0
        self.guests = []
        self.songs = []
    
    def guest_count(self):
        return len(self.guests)
    
    def add_guest(self, guest):
        self.guests.append(guest)

    def remove_guest(self, id):
        for guest in self.guests:
            if id == guest.id:
                self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)
