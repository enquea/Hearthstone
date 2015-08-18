import json

with open('AllSets.json') as f:
    data = json.load(f)

#sets = ['Basic', 'Classic', 'Curse of Naxxramas', 'Blackrock Mountain', 'Goblins vs Gnomes']

mapping = {}
for name, set_list in data.iteritems():
    for item in set_list:
        card_id = item.get('id')
        card_name = item.get('name')
        if card_id and card_name:
            mapping[card_id] = card_name

import pdb; pdb.set_trace()

with open('id_name_map.json', 'w+') as f:
    json.dump(mapping, f)

