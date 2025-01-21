from osu_db_tools import buffer
from tqdm import tqdm


def parsedb(osudb, file):
    dbmaps = []
    with open(osudb, "rb") as db:
        version = buffer.read_uint(db)
        folder_count = buffer.read_uint(db)
        account_unlocked = buffer.read_bool(db)
        buffer.read_uint(db)
        buffer.read_uint(db)
        name = buffer.read_string(db)
        num_beatmaps = buffer.read_uint(db)

        for index in tqdm(range(num_beatmaps)):
            artist = buffer.read_string(db)
            artist_unicode = buffer.read_string(db)
            song_title = buffer.read_string(db)
            song_title_unicode = buffer.read_string(db)
            mapper = buffer.read_string(db)
            difficulty = buffer.read_string(db)
            audio_file = buffer.read_string(db)
            md5_hash = buffer.read_string(db)
            map_file = buffer.read_string(db)
            ranked_status = buffer.read_ubyte(db)
            num_hitcircles = buffer.read_ushort(db)
            num_sliders = buffer.read_ushort(db)
            num_spinners = buffer.read_ushort(db)
            last_modified = buffer.read_ulong(db)
            approach_rate = buffer.read_float(db)
            circle_size = buffer.read_float(db)
            hp_drain = buffer.read_float(db)
            overall_difficulty = buffer.read_float(db)
            slider_velocity = buffer.read_double(db)
            # skip these int float pairs
            i = buffer.read_uint(db)
            for _ in range(i):
                buffer.read_int_float(db)

            i = buffer.read_uint(db)
            for _ in range(i):
                buffer.read_int_float(db)

            i = buffer.read_uint(db)
            for _ in range(i):
                buffer.read_int_float(db)

            i = buffer.read_uint(db)
            for _ in range(i):
                buffer.read_int_float(db)

            drain_time = buffer.read_uint(db)
            total_time = buffer.read_uint(db)
            preview_time = buffer.read_uint(db)
            # skip timing points
            # i = buffer.read_uint(db)
            for _ in range(buffer.read_uint(db)):
                buffer.read_timing_point(db)
            beatmap_id = buffer.read_uint(db)
            beatmap_set_id = buffer.read_uint(db)
            thread_id = buffer.read_uint(db)
            grade_standard = buffer.read_ubyte(db)
            grade_taiko = buffer.read_ubyte(db)
            grade_ctb = buffer.read_ubyte(db)
            grade_mania = buffer.read_ubyte(db)
            local_offset = buffer.read_ushort(db)
            stack_leniency = buffer.read_float(db)
            gameplay_mode = buffer.read_ubyte(db)
            song_source = buffer.read_string(db)
            song_tags = buffer.read_string(db)
            online_offset = buffer.read_ushort(db)
            title_font = buffer.read_string(db)
            is_unplayed = buffer.read_bool(db)
            last_played = buffer.read_ulong(db)
            is_osz2 = buffer.read_bool(db)
            folder_name = buffer.read_string(db)
            last_checked = buffer.read_ulong(db)
            ignore_sounds = buffer.read_bool(db)
            ignore_skin = buffer.read_bool(db)
            disable_storyboard = buffer.read_bool(db)
            disable_video = buffer.read_bool(db)
            visual_override = buffer.read_bool(db)
            last_modified2 = buffer.read_uint(db)
            scroll_speed = buffer.read_ubyte(db)

            dbmaps.append(beatmap_set_id)

    with open(file, "w") as fp:
        for item in list(set(dbmaps)):
            fp.write("%s\n" % item)
    # there are alot of other information that can be captured with the above apis
