from ossapi import Ossapi 
import os
import json


# Initialize the API
with open('config.json', 'r') as config_file: 
    config = json.load(config_file)

api = Ossapi(config['client_id'], config['client_secret'])


# Reads the list of previously scanned ranked maps
def load_prev(file):
    if not os.path.exists(file): # if file doesn't exist, create it
        with open(file, 'w') as fp: pass
    with open(file, 'r') as fp:
        prev_maps = fp.read().split("\n") 
    return prev_maps


def run_scan(prev, file): #update the ranked beatmapset list
    prev_cursor = None 
    newly_ranked_maps = []
    print(f'{len(prev)} mapsets already saved, scanning for new mapsets...')

    while True: # loop scan for newly ranked maps
        query = api.search_beatmapsets(mode=0, category='ranked', cursor=prev_cursor)
        prev_cursor = query.cursor
        batch_ids = [str(item.id) for item in query.beatmapsets]
        batch_ids = [x for x in batch_ids if x not in prev] #remove all already existing maps
        if len(batch_ids) == 0: 
            if len(newly_ranked_maps) == 0: 
                print('no new mapsets found')
            else: 
                print(f'finished search, found {len(newly_ranked_maps)} new mapsets')
            break
        newly_ranked_maps.extend(batch_ids)

    newly_ranked_maps.extend(prev)

    with open(file, 'w') as fp:
        for item in newly_ranked_maps:
            fp.write("%s\n" % item)
