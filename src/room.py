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
