class Player:
    side = None
    inventory = []
    visited_items = []
    used_items = []

    def __init__(self) -> None:
        pass

    def visit_item(self, item):
        self.visited_items.append(item)

    def use_item(self, item):
        self.used_items.append(item)
