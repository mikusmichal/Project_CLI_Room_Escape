import hashlib

from Player import Player


class Item:
    data = None
    name = None

    def __init__(self, name, data) -> None:
        self.name = name
        self.data = data

    def contains_item(self, contained: 'Item', player: Player):
        if self not in player.visited_items:
            return False
        for item_2 in self.data['items']:
            if item_2.contains_item(contained, player):
                return True
        return contained in self.data['items']

    def is_on_side(self, side, player: Player):
        for item_2 in side['items']:
            if item_2.contains_item(self, player):
                return True
        return self in side['items']

    def use(self, side, player: Player, second_item: 'Item' = None):
        if not self.is_on_side(side, player):
            print("There is no {:s} on this side.".format(self.name))
            return

        print("You can't use this item.")


class SuitCase(Item):
    def use(self, side, player: Player, second_item: 'Item' = None):
        if not self.is_on_side(side, player):
            print("There is no {:s} on this side.".format(self.name))
            return

        code_hash = self.data['code']
        input_code = input('Now you are trying to unlock this suitcase. Type "end" to stop trying.\n')
        while input_code != 'end':
            m = hashlib.sha256()
            m.update(bytearray(input_code, 'utf8'))
            input_code_hash = m.digest()
            if code_hash == input_code_hash:
                print('Congratz, you unlocked the suitcase')
                player.visit_item(self)
                player.use_item(self)
                break
            else:
                print('This is wrong code')
                input_code = input('Now you are trying to unlock this suitcase. Type "end" to stop trying.\n')

        print("There is a security card. You can take it and use it to unlock the doors.")


class Door(Item):
    def use(self, side, player: Player, second_item: 'Item' = None):
        if not self.is_on_side(side, player):
            print("There is no {:s} on this side.".format(self.name))

        if 'card' not in player.inventory:
            print("These doors are locked. Sorry. You need a security card.")
        else:
            player.use_item(self)
        return
