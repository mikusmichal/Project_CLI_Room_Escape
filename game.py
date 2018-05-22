from Action import MoveLeftAction, MoveRightAction, ExamineAction, TakeAction, UseAction, ShowInventoryAction, HelpAction, CheatAction
from Item import Item, SuitCase, Door
from Player import Player
from Objects import sides_keys, sides, items_data
from utils import clear_screen

if __name__ == '__main__':
    player = Player()
    player.side = 0

    items = {}
    for item_name, item_data in items_data.items():
        if item_name == 'suitcase':
            items[item_name] = SuitCase(item_name, item_data)
        elif item_name == 'door':
            items[item_name] = Door(item_name, item_data)
        else:
            items[item_name] = Item(item_name, item_data)

    for key, item in items.items():
        contained_items = []
        for item_name in item.data['items']:
            contained_items.append(items[item_name])
        item.data['items'] = contained_items

    winning_used_item = items['door']

    for key in sides.keys():
        items_on_side = []
        for item_name in sides[key]['items']:
            items_on_side.append(items[item_name])
        sides[key]['items'] = items_on_side

    actions = [
        MoveLeftAction(items),
        MoveRightAction(items),
        ExamineAction(items),
        TakeAction(items),
        UseAction(items),
        ShowInventoryAction(items),
        CheatAction,
        HelpAction
    ]

    print("""
WELCOME

Mildly prepare to enter mildly challenging game

In this game you have to escape the room for no reason. (maybe because there is no fridge)

You can see full list of commands by writing 'help'.

You can use 'left' and 'right' to change your directory and then write commands like 'examine sky'
or 'use food me', or rather different objects, because there are no windows and sadly no fridge.

You can also turn this game off and get a life, but seriously, who would do that?

Now press "ENTER" and try it out!

    """)

    winning = False
    print("Possible actions are: " + ', '.join([a.name for a in actions]) + "\n\n If you find more of them, please tell us!")
    input("\n")
    clear_screen()
    while not winning:
        print("Now you are facing {:s}.".format(sides_keys[player.side]))
        side = sides[sides_keys[player.side]]
        print(side['description'])
        print("What do you want to do, filthy human?\nType 'left' or 'right' to change directions.")

        user_input = input("\n")
        clear_screen()

        words = user_input.split(' ')
        action_input = words[0]

        available_action = [a for a in actions if a.name == action_input or a.short_name == action_input]
        if len(available_action) == 0:
            print("Try it again, next time you can be lucky!")
            continue

        if len(words) > 1:
            item = items[words[1]]
        else:
            item = None

        if len(words) > 2:
            second_item = items[words[2]]
        else:
            second_item = None

        action = available_action[0]

        action.perform(player, side, item, second_item)

        winning = winning_used_item in player.used_items

    print("""
Did you really win? Let me see... Yeah, you really did! Congratz!

Please, support us by giving us your feedback or your soul!

If you liked the game, you are probably mentally ill, but the good news are that   
you can expect us to make another game, newly including good story or good humor.
(otherwise we would run out of budget)

You may play this again to make sure it didn't change or recommend it to you friends.

Anyway, thank you for playing!
    """)
    input("\n")
