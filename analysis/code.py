# find out if class is druid
# find out what turn ramp is played
# find out win/loss

import collections
import re
import pprint

logfile = 'output_log.txt'

players = collections.defaultdict(dict)

def set_key_value_by_player_name(match, key):
    """
    Takes a 'key' string and sets value in players dict
    """
    entity = match.group(1)
    value = match.group(2)
    players[entity][key] = value

with open(logfile) as f:
    # each line has entity, which is the player name
    # mapped to things like:
    # player_id
    # win/loss
    turn = 0

    for line in f:
        # turn 
        match = re.search(r'cardId=HERO_\d+ player=(1|2)] tag=NUM_TURNS_IN_PLAY value=(\d+)', line)
        if match:
            print match.group()

        # wild growth
        match = re.search(r'tag=JUST_PLAYED .* zone=PLAY zonePos=0 cardId=CS2_013 player=(1|2)]', line)
        if match:
            print match.group()

        #entity - first player
        match = re.search(r'Entity=(.*) tag=FIRST_PLAYER value=(\d)', line)
        if match:
            set_key_value_by_player_name(match, 'first')

        #entity - player id
        match = re.search(r'Entity=(.*) tag=PLAYER_ID value=(1|2)', line)
        if match:
            set_key_value_by_player_name(match, 'id')

        #entity - win/loss 
        match = re.search(r'Entity=(.*) tag=PLAYSTATE value=(WON|LOST)', line)
        if match:
            set_key_value_by_player_name(match, 'result')

        #class - player id
        match = re.search(r'cardId=(HERO_\d+) player=(1|2)', line)
        if match:
            hero = match.group(1)
            id = match.group(2)
            players[id]['hero'] = hero

#pprint.pprint(dict(players))
