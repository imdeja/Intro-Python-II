from room import Room
from player import Player
from item import Item
import textwrap
import csv

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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
# Textwrap
wrapper = textwrap.TextWrapper(width=65)

# Make a new player object that is currently in the 'outside' room.
player_name = input("What is your character's name?: ")
new_player = Player(player_name, room['outside'])

# Get item names and return ids
def get_id(names):
    split = names.split(",")
    base = ""
    for item in split:
        base = base + "'" + item.replace(" ", "").lower() + "',"
    return eval("[" + base + "]")

# Get items from list
list_of_items = {}

with open("src/list_of_items.txt", "r") as f:
    for line in f:
        data = eval(line)
        list_of_items[data["id"]] = Item(data["name"], data["description"])

# Put items in rooms
foyer_items = [list_of_items["mastersword"], list_of_items["map"]]
room["foyer"].add_items(foyer_items)

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

while(True):
    # Find current room
    current_room = new_player.current_room

    # Print current description
    print("Current Room: {}".format(current_room.name))
    [print(line) for line in wrapper.wrap(text=current_room.description)]
    item_str = "Items in room:\t{}".format(current_room.check_items())
    [print(line) for line in wrapper.wrap(text=item_str)]

    # Input 
    inp = input(
        "What would you like to do? [Directions:'n', 'e', 's', 'w'  Actions: 'take', 'get', 'remove', 'drop', 'i', 'inventory']"
    )

    # Preprocess 
    inputs = inp.split(maxsplit=1)

    # Process 
    if(len(inputs) == 1):
        inp = inputs[0]
        if(inp in ['q']):
            break
        
        elif(inp in ['n', 'e', 's', 'w']):
            new_player.move_player(inp)
            
        if inp in ["i", "inventory"]:
            print("Inventory:")
            [print(line) for line in new_player.get_items()]
        
    elif len(inputs) == 2:
        verb, obj = inputs[0], inputs[1]
        if verb in ["take", "get"]:
            # List of ids
            id_list = get_id(obj)
            # Remove items from room
            removed_items_ids, removed_items = current_room.remove_items(id_list)
            # Add items to inventory
            new_player.add_items(removed_items)
        
        if verb in ["remove", "drop"]:
            id_list = get_id(obj)
            # Remove items from player
            removed_item_ids, removed_items = new_player.remove_items(id_list)
            # Add items to room
            items = {id: item for id, item in zip(removed_item_ids, removed_items)}
            current_room.add_items(removed_items)

    else:
        print('Invalid Input')
