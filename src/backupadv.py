'''while True:
    current = newPlayer.room
    items = newPlayer.room.roomItems
    print(
        f"\n****Hello {newPlayer.name}. your current location is {current}****")
    print(f"\nItems in the area:")
    for i in items:
        print(i)
    print('-------------------------------------------------------')
    choice = input(
        f"what would you like to do? Move: [n, e, s, w] Interact: [pickup (item), drop (item), i(inventory)] q(quit): ")
    if choice == "n":
        if current.n_to == None:
            print("\n**There's nothing there!**")
        elif current.n_to == room['hidden']:
            if item['rope'] in newPlayer.inventory:
                print(
                    '\nYou manage to throw your rope and hook it on some rocks then swing across!')
                newPlayer.room = current.n_to
            else:
                print('\nYou need a rope!')
        else:
            newPlayer.room = current.n_to
    elif choice == "e":
        if current.e_to == None:
            print("\n**There's nothing there!**")
        else:
            newPlayer.room = current.e_to
    elif choice == "s":
        if current.s_to == None:
            print("\n**There's nothing there!**")
        elif current.s_to == room['overlook']:
            if item['rope'] in newPlayer.inventory:
                print(
                    '\nYou manage to throw your rope and hook it on some rocks then swing across!')
                newPlayer.room = current.s_to
            else:
                print('\nYou need a rope!')
        else:
            newPlayer.room = current.s_to
    elif choice == "w":
        if current.w_to == None:
            print("\n**There's nothing there!**")
        else:
            newPlayer.room = current.w_to
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
        print("\nForbidden movement input.")'''
