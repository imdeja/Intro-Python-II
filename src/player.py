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

    def add_items(self, list_of_items):
        for item in list_of_items:
            item.on_take()
            self.items[item.id] = item

    def remove_items(self, item_id_list):
        # Keep object type as list
        if type(item_id_list) != list:
            raise TypeError("Needs to be a list!")

        # Check if id's are in the room's dict
        if any([id in self.items for id in item_id_list]):
            # Results of trying to remove items
            status = []
            removed_items = []

            for id in item_id_list:
                try:
                    # Delete key
                    item = self.items.pop(id)

                    item.on_drop()
                    removed_items.append(item)
                    # The item will be deleted and read True
                    status.append(True)
                except KeyError as ke:
                    # If it's is not found, it will read False
                    status.append(False)

            # Items from list removed from dict
            removed_item_ids = [
                item for item, removed in zip(item_id_list, status) if removed
            ]

            return (removed_item_ids, removed_items)
        else:
            return ([], [])

    def __repr__(self):
        return self.__dict__

    def __str__(self):
        s = ""
        l = ["{}:{}".format(key, value) for key, value in self.__dict__.items()]
        s = "\n".join(l)
        return s
