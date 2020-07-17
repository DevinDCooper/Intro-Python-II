from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",Item('bow')),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",Item('sword')),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", Item("water")),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", Item("shield")),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", Item('gold')),
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

player_name = input("What is your name: ")
player_room = room["outside"]
player = Player(player_name, player_room)
print(player)
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
    current_room = player.current_room
    player_inventory = [x.name for x in player.inventory] if len(player.inventory) else "Empty Bag"
    room_inventory = [ x.name for x in current_room.item] if len( current_room.item) else "Empty Room"



    print(f'You are located at {current_room.name} and {current_room.description}')
    print(f"You have found a {room_inventory}\n")
    print(f"If you would like to take an item, type: take item_name\n")
    print(f"If you would like to drop an item, type: drop item_name\n")

    print(f'{player_name} has {len(player.inventory)} item(s) in there bag\n')
    print(f'Bag: {player.inventory}')
    print("Choose next path.\n")

    enter = input('Enter n, s , e, w and q to quit the game: ')

    action = enter[0:4]
    item = enter[5: ]

    if enter == 'q':
            print(f'Thanks for playing, {player_name}. Till next time!')
    if enter == 'n':
        if hasattr(current_room, 'n_to'):
            print("going North")
            player.current_room = current_room.n_to
        else:
            print(f'{player_name} enter another location, you hit a invisible wall ')
    elif enter == 's':
        if hasattr(current_room, 's_to'):
            print(f'{player_name} you are going South my friend')
            player.current_room = current_room.s_to
        else:
            print(f'{player_name} enter another location, you hit a invisible wall ')
    elif enter == 'e':
        if hasattr(current_room, 'e_to'):
            print(f'{player_name} you are moving East!')
            player.current_room = current_room.e_to
        else:
            print(f'{player_name} enter another location, you hit a invisible wall ')
    elif enter == 'w':
        if hasattr(current_room, 'w_to'):
            print(f'{player_name} going out West')
            player.current_room = current_room.w_to
            print(f'{player_name} enter another location, you hit a invisible wall ')

    elif action == "drop":
        item_name_list = [i.name for i in player_inventory]
        item_index = item_name_list.index(item)
        current_room.add_item(player.inventory[item_index])
        player.drop(item_index)

    elif action == "take" :
        item_name_list = [i.name for i in current_room.item]
        item_index = item_name_list.index(item)
        player.take(current_room.item[item_index])
        current_room.delete_item(item_index)


    else:
            print('Please enter a valid location')
            break


