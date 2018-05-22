

sides_keys = {
        0: 'north',
        1: 'east',
        2: 'south',
        3: 'west',
    }

sides = {
        'north': {
            'description': "This is the northern wall with goddamn big door that you need to open.",
            'items': [
                'door'
            ]
        },
        'east': {
            'description': "This is the eastern wall. There is a cabinet. Maybe it is empty, but why would we do that?",
            'items': [
                'cabinet'
            ]
        },
        'south': {
            'description': "This is the southern wall. There is shelf. Interesting, huh? I think that steel "\
            "suitcase is more interesting.",
            'items': [
                'shelf', 'suitcase'
            ]
        },
        'west': {
            'description': "This is the western wall. There may be cowboys, but more likely only a desk."\
            "Important desk.",
            'items': [
                'desk'
            ]
        }
    }
items_data = {
        'cabinet': {
            'description': "It's a locked wooden cabinet. There is a piece of paper inside and a dusty picture on "\
            "the top. The paper looks important.",
            'items': ['paper', 'picture']
        },
        'paper': {
            'description': "Paper says: If you are stuck with numbers, remember: \n\nThe path of the righteous man is "\
            "beset on all sides by the inequities of the selfish and the tyranny of evil men. Blessed is he who, in "\
            "the name of charity and good will, shepherds the weak through the valley of the darkness.",
            'items': []
        },
        'picture': {
            'description': "It's a picture of turtle. I only wonder why is it on its back?",
            'items': []
        },
        'desk': {
            'description': "It's a wooden desk with lamp and a photo.",
            'items': ['lamp', 'photo'
                      ]
        },
        'lamp': {
            'description': "Magic lamp. Maybe it will be useful somehow.",
            'items': []
        },
        'photo': {
            'description': "It's a photo of a mystery man with a camera. Interesting.",
            'items': []
        },
        'shelf': {
            'description': "It's a wooden shelf with a key. No, it isn't THAT key, but you can still use it somewhere.",
            'items': [
                'key'
            ]
        },
        'key': {
            'description': "It'a a key. But it won't unlock the door. Did you think it would be so easy?",
            'items': []
        },
        'suitcase': {
            'description': "It has a 4-digit lock. You can use it try out 10 000 combinations or quess the right one.",
            'items': [
                'card'
            ],
            'code': b'\xc3\x11N?w\x1d_i\x17!,\x9f\x0b\xc78K\r+\x14\xf3s\x18H\xd2\x13\xad\\\x9a\xacV\x14M'
        },
        'card': {
            'description': "It is a security card that unlocks that goddamn big door. Attention: Use it only when you are prepared for the cruel world!",
            'items': [
                'card'
            ]
        },
        'door': {
            'description': "It is door.",
            'items': []
        },
    }
