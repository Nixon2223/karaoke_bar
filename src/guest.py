class Guest:
    def __init__(self, id, wallet, favourite_song):
        self.id = id
        self.wallet = wallet
        self.favourite_song = favourite_song
    
    def decrease_wallet(self, amount):
        self.wallet -= amount