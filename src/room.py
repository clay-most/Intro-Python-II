# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        return f"They are {self.name}. {self.description}"
    def get_item(self, var):
        for item in self.items:
            if item.name.lower() == var.lower():
                return item
        return None