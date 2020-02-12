from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", """North of you, the cave mount beckons"""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but you will need a rope to cross the chasm!"""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been looted by
earlier adventurers. All that is left is a single piece of gold. The only exit is to the south."""),

    'hidden': Room("Hidden Room", """You've managed to cross the overlook and find a hidden room!""")
}

# Declare items

item = {
    'sword': Item("sword", "A small but sharp sword."),
    'staff': Item("staff", "A slightly magical stick."),
    'gold': Item('gold', "Lovely money!"),
    'rope': Item('rope', "A bunch of rope."),
    'lantern': Item('lantern', "How is this thing working?"),
    'trout': Item('trout', "Somehow still fresh.")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['overlook'].n_to = room['hidden']
room['hidden'].s_to = room['overlook']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Add items to rooms

room['outside'].add_item(item['sword'])
room['foyer'].add_item(item['staff'])
room['overlook'].add_item(item['lantern'])
room['narrow'].add_item(item['rope'])
room['foyer'].add_item(item['trout'])
room['treasure'].add_item(item['gold'])


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


def check_move(move):
    current = newPlayer.room
    if current.__dict__[f'{move}_to'] == None:
        print("\n**There's nothing there!**")
    elif current.__dict__[f'{move}_to'] == room['hidden']:
        if item['rope'] in newPlayer.inventory:
            print(
                '\nYou manage to throw your rope and hook it on some rocks then swing across!')
            newPlayer.room = current.__dict__[f'{move}_to']
        else:
            print('\nYou need a rope!')
    elif current.s_to == room['overlook']:
        if item['rope'] in newPlayer.inventory:
            print(
                '\nYou manage to throw your rope and hook it on some rocks then swing across!')
            newPlayer.room = current.s_to
        else:
            print('\nYou need a rope!')
    else:
        newPlayer.room = current.__dict__[f'{move}_to']


while True:
    current = newPlayer.room
    items = newPlayer.room.roomItems
    movement_choice = ['n', 'e', 's', 'w']
    print(
        f"\n****Hello {newPlayer.name}. your current location is {current}****")

    print(f"\nItems in the area:")
    for i in items:
        print(i)
    print('-------------------------------------------------------')
    choice = input(
        f"what would you like to do? Move: [n, e, s, w] Interact: [pickup (item), drop (item), i(inventory)] q(quit): ")
    if choice in movement_choice:
        check_move(choice)
    elif choice == "i" or choice == "inventory":
        print("\nInventory:")
        for i in newPlayer.inventory:
            print(i)
    elif choice.split()[0] == "pickup":
        item_choice = choice.split()[1]
        if item_choice in item.keys():
            if item[item_choice] in items:
                newPlayer.pickup(item[item_choice])
                current.remove_item(item[item_choice])
                item[item_choice].on_take()
            else:
                print("\nItem isn't in this room.")
        else:
            print('\nItem does not exist!')
    elif choice.split()[0] == "drop":
        item_to_drop = choice.split()[1]
        if item_to_drop in item.keys():
            if item[item_to_drop] in newPlayer.inventory:
                newPlayer.drop_item(item[item_to_drop])
                current.add_item(item[item_to_drop])
                item[item_to_drop].on_drop()
            else:
                print(f"\nYou don't own a {item[item_to_drop].name}")
        else:
            print("\nThat item doesn't exist.")
    elif choice == "q":
        print("Thanks for playing!")
        exit()
    else:
        print("\nForbidden movement input.")
