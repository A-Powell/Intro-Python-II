from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", """North of you, the cave mount beckons"""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
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
newPlayer = Player('Austin', room['outside'])



# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    current = newPlayer.room
    print(f"****Hello {newPlayer.name}. your current location is {current}****")
    print('-------------------------------------------------------')
    choice = input(f"which direction would you like to go? [n, e, s, w, q to quit]: ")
    print('-------------------------------------------------------')
    if choice == "n":
        if current.n_to == None:
            print('-------------------------------------------------------')
            print("**There's nothing there!**")
            print('-------------------------------------------------------')
        else:
            newPlayer.room = current.n_to
    elif choice == "e":
        if current.e_to == None:
            print('-------------------------------------------------------')
            print("**There's nothing there!**")
            print('-------------------------------------------------------')
        else:
            newPlayer.room = current.e_to
    elif choice == "s":
        if current.s_to == None:
            print('-------------------------------------------------------')
            print("**There's nothing there!**")
            print('-------------------------------------------------------')
        else:
            newPlayer.room = current.s_to
    elif choice == "w":
        if current.w_to == None:
            print('-------------------------------------------------------')
            print("**There's nothing there!**")
            print('-------------------------------------------------------')
        else:
            newPlayer.room = current.w_to
    elif choice == "q":
        print("Thanks for playing!")
        exit()
    else:
        print('-------------------------------------------------------')
        print("Forbidden movement input.")
        print('-------------------------------------------------------')