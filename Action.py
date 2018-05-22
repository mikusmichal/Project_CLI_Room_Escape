from Item import Item
from Player import Player



class Action:
    name = None
    short_name = None
    items = None

    def __init__(self, items) -> None:
        super().__init__()
        self.items = items

    def perform(self, player: Player, side: str, item: Item=None, second_item: Item=None):
        pass

    def is_valid(self, player: Player, side, item: Item=None, second_item: Item=None):
        pass


class MoveLeftAction(Action):
    name = 'left'
    short_name = 'l'

    def perform(self, player: Player, side, item: Item=None, second_item: Item=None):
        player.side = (player.side - 1) % 4


class MoveRightAction(Action):
    name = 'right'
    short_name = 'r'

    def perform(self, player: Player, side, item: Item=None, second_item: Item=None):
        player.side = (player.side + 1) % 4


class ExamineAction(Action):
    name = 'examine'
    short_name = 'exam'

    def perform(self, player: Player, side, item: Item=None, second_item: Item=None):
        if not self.is_valid(player, side, item, second_item):
            if item is None:
                print("Please specify which item you want to examine.")
                return
            print("There is no {:s} on this side.".format(item.name))

            return

        if item.name != 'suitcase':
            player.visit_item(item)
        print(item.data['description'])

    def is_valid(self, player: Player, side, item: Item=None, second_item: Item=None):
        if item is None:
            return False
        if (not item.is_on_side(side, player)) and (item.name not in player.inventory):
            return False
        else:
            return True


class UseAction(Action):
    name = 'use'
    short_name = 'u'

    def __init__(self, items) -> None:
        super().__init__(items)

    def perform(self, player: Player, side, item: Item=None, second_item: Item=None):
        item.use(side, player, second_item)
        return


class TakeAction(Action):
    name = 'take'
    short_name = 't'

    def perform(self, player: Player, side, item: Item=None, second_item: Item=None):

        if not self.is_valid(player, side, item, second_item):

            if not item.is_on_side(side, player):
                print("There is no {:s} on this side.".format(item.name))
                return
            if not second_item.is_on_side(side, player):
                print("There is no {:s} on this side.".format(item.name))
                return
            if second_item not in self.items[item.name].data['items']:
                print("There is no {:s} in/on {:s}".format(second_item.name, item.name))
                return

        player.inventory.append(second_item.name)
        print("You took the {:s}".format(second_item.name))

    def is_valid(self, player: Player, side, item: Item=None, second_item: Item=None):

        if second_item is None:
            print("You have to write two items after 'take'")
            return False
        if not item.is_on_side(side, player):
            print("There is no {:s} on this side.".format(item.name))
            return False
        if not second_item.is_on_side(side, player):
            print("There is no {:s} on this side.".format(item.name))
            return False

        return True


class ShowInventoryAction(Action):
    name = 'show'
    short_name = 's'

    def perform(self, player: Player, side, item: Item=None, second_item: Item=None):
        print("Your inventory contains: " + ', '.join(player.inventory))


class HelpAction(Action):
    name = 'help'
    short_name = 'h'

    def perform(self, player: Player, side, item: Item=None, second_item: Item=None):
        print("Possible actions are: " + ', '.join([a.name for a in Action.__subclasses__()]))
        print("'take' is used in the form take-from where-what, 'use' only use-what.")
        print("If you don't know how to win the game, you can use action 'cheat'")


class CheatAction:
    name = 'cheat'
    short_name = 'ch'

    def perform(self, player: Player, side, item: Item=None, second_item: Item=None):
        print("You need to examine paper, then search for a 4 digit number that fits the clue.\nThen use suitcase, write number, take suitcase card, use door and viola, you won!")
