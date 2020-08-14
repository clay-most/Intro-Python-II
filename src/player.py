# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []
    def travel(self, direction):
        destination = getattr(self.location, f"{direction}_to")
        if destination == None:
            print("That is impossible")
        else:
            self.location = destination
    def get(self, item):
        self.inventory.append(item)
        print(f"Inventory: {self.inventory}")
    def drop(self, item):
        self.inventory.remove(item)
        print(f"Inventory: {self.inventory}")