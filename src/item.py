class Item:
    def __init__(self, name, description):
        self.id = name.replace(" ", "").lower()
        self.name = name
        self.description = description

    def on_take(self, action=None):
        print("You picked up {}".format(self.name))
        if action is None:
            pass
        else:
            pass

    def on_drop(self, action=None):
        print("You dropped {}".format(self.name))
        if action is None:
            pass
        else:
            pass