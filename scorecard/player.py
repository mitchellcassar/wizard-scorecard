class Player():
    def __init__(self):
        self.name = ''
        self.bid = 0
        self.total = 0
        self.tricks_taken = 0
        
    
    def get_name(self):
        self.name = input('please enter player name: ')

    def __lt__(self, other):
        return self.total < other.total


