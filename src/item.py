class Item:
    def __init__(self, name, description):
        self.name = name
        self. description = description
    def on_take(self, player):
        print (f"{player.name} picked up {self.name}")