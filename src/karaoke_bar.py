class Karaoke_Bar:
    def __init__(self, name, entry_fee):
        self.name = name
        self.entry_fee = entry_fee
        self.rooms = []
    
    def sell_entry(self, guest, room):
        if room.guest_count() < room.capacity:
            room.add_guest(guest)
            guest.decrease_wallet(self.entry_fee)
            
