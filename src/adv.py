from room import Room
from player import Player
import textwrap

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

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
while(True):
    # Find current room
    current_room = new_player.current_room

    # Print current description
    print('Current Room: {}'.format(current_room.name))
    [print(line) for line in wrapper.wrap(text=current_room.description)]

    # Input 
    inp = input('What direction would you like to go? ')

    # Preprocess 
    inputs = inp.split(maxsplit=1)

    # Process 
    if(len(inputs) == 1):
        inp = inputs[0]
        if(inp in ['q']):
            break

        elif(inp in ['n', 'e', 's', 'w']):
            new_player.move_player(inp)

    else:
        print('Invalid Input')
#
# If the user enters "q", quit the game.
