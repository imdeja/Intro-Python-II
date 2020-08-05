# Write a class to hold player information, e.g. what room they are in
# currently.
class WrongWay(Exception):
    def __init__(self, room, direction):
        self.room = room
        self.direction = direction


class Player:
    def __init__(self, name, current_room, starting_items=None):
        self.name = name
        self.current_room = current_room
        if(starting_items is None):
            self.items = {}
        else:
            self.items = starting_items

    # Get items in a player's inventory
    def get_items(self):
        if(len(self.items) == 0):
            return ['No items']
        else:
            lines = []
            for item in self.items.values():
                s = 'Name: {}\n\t{}'.format(item.name, item.description)
                lines.append(s)
            return lines


    # Move player to new room based on input
    def move_player(self, target_dir):
        try:
            # Make sure there is a room from desired input
            target_room = getattr(
                self.current_room, '{}_to'.format(target_dir))
            if(target_room is None):
                raise WrongWay(self.current_room, target_dir)

            # Move player to target room
            self.current_room = target_room

        # Player moves wrong way error
        except WrongWay as error:
            print('Invalid direction!')
