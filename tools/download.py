from urllib.request import urlretrieve
from tqdm import tqdm
import os
import time

def download_maps(beatmapset_ids, db_ids, dir):

    # Check if the directory exists, if notcreate it
    if not os.path.exists(dir):
        os.makedirs(dir)
        print(f"Directory '{dir}' did not exist. Created it.")

    # read in the values
    with open(beatmapset_ids, 'r') as fp:
        all_maps = fp.read().split("\n") 

    with open(db_ids, 'r') as fp:
        db_maps = fp.read().split("\n") 

    items_not_in_db = [item for item in all_maps if item not in db_maps] 
    print(f'A total of {len(items_not_in_db)} maps are missing, downloading missing maps')

    for set_id in tqdm(items_not_in_db):
        if not os.path.isfile(f'{dir}{set_id}.osz'): # Check if already exist in download folder
            try: 
                time.sleep(1) # Prevent rate limiting 
                urlretrieve(f'https://api.nerinyan.moe/d/{set_id}?noVideo=true&NoHitsound=true&NoStoryboard=true', f'{dir}{set_id}.osz') 
            except Exception as e: 
                print(f'Failed retriving {set_id}\n Error Message: {e}')
                time.sleep(30) # Wait for rate limit

    print(f'finished downloading')
