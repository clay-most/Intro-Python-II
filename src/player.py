# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def travel(self, direction):
        destination = getattr(self.location, f"{direction}_to")
        if destination == None:
            print("That is impossible")
        else:
            self.location = destination
