# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        if items is None:
            self.items = {}
        else:
            self.items = {item.id: item for item in items}

        # Room direction
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    # Return values from item dictionary 
    def view_items(self):
        return items.items()
    
    # Current items in the room
    def check_items(self):
        if self.items is None:
            return "This room is empty"
        else:
            base = ""
            for item in self.items:
                base = base + self.items[item].name + ", "
            return base[:-2]

    def add_items(self, list_of_items):
        # Keep object type as list
        if type(list_of_items) != list:
            raise TypeError("Needs to be a list!")

        # Add Item to the dict
        for item in list_of_items:
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
            return []
