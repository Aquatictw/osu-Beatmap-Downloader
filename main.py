import json
from tools.scan_newmaps import * 
from tools.read_db import * 
from tools.download import * 

def main():
    # Initialize path values
    with open('config.json', 'r') as config_file: 
        config = json.load(config_file)

    beatmapset_ids_path = config['beatmapset_ids_path'] # file containing ranked beatmapset ids
    db_ids_path = config['db_ids_path'] # file containing beatmap ids from osu!.db
    db_path = config['db_path'] # osu!.db file path
    download_path = config['download_path'] # download path for beatmaps

    # update the ranked beatmap list
    prev = load_prev(beatmapset_ids_path) 
    run_scan(prev, beatmapset_ids_path)

    #extract information from osu!.db
    print('parsing osu!.db')
    parsedb(db_path, db_ids_path)
    print('finished parsing osu!.db')

    #download missing beatmaps 
    download_maps(beatmapset_ids_path, db_ids_path, download_path)

if __name__ == "__main__":
    main()
