from room import Room
from player import Player

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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

print(f"\nTo travel North enter n, to travel East enter e, ect.\n")
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
    command= input(f"Which direction will {player.name} go?\n").lower()
    if command in ["n","s","e","w"]:
        player.travel(command)
        print(f"\n{player.name} looks around. {player.location}\n")
    elif command == "q":
        print("Good bye, traveler")
        quit()
    else:
        print("valid commands are n, s, e, w, q.")