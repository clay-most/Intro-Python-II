from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside the Cave Entrance",
                     "North of them, the cave mouth beckons"),

    'foyer':    Room("in the Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("at an Grand Overlook", """A steep cliff appears before them, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("in a Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("in the Treasure Chamber", """They've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

#Create items

item = {
    "ring":Item("ring","magic ring"),
    "carrot":Item("carrot","normal carrot"),
    "sword": Item("sword","rusty sword"),
    "rope": Item("rope","frayed rope"),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#Add items to rooms

room["foyer"].items.append(item["ring"])

#
# Main
#

print(f"\nTo travel North enter n, to travel East enter e, ect.\n")

# Make a new player object that is currently in the 'outside' room.
playerName = input("Welcome, traveler.\nPlease enter your name\n")
player = Player(playerName, room["outside"])
print(f"\nGood Luck, {player.name}\n{player.name} looks around. {player.location}\n")


# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    command= input(f"What will {player.name} do?\n").lower()
    if command in ["n","s","e","w"]:
        player.travel(command)
        print(f"\n{player.name} looks around. {player.location}\n")
        if len(player.location.items)>0:
            print (f"In this room there is a...") 
            for item in player.location.items: 
                print (f"{item.name} ({item.description}).\nTo pick up type (get {item.name})")
    elif "get" in command:
        checkItem = player.location.get_item(command[4:])
        if checkItem:
            checkItem.on_take(player)
            player.get(checkItem)
            player.location.items.remove(checkItem)
        else:
             print (f"{command[4:]} is not in this room")
    elif "drop" in command:
        if command[5:] in player.inventory:
            player.drop(command[5:])
        else:
            print(f"That item is not in {player.name}'s pack.")
    elif command == "q":
        print("Good bye, traveler")
        quit()
    else:
        print("valid commands are n, s, e, w, q.")