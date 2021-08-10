import configparser

# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')
ACCESS_KEY_ID = config.get("SECRETS", "ACCESS_KEY_ID")
SECRET_ACCESS_KEY = config.get("SECRETS", "SECRET_ACCESS_KEY")
DWH_REGION = config.get("IAM_ROLE","REGION")
DWH_IAM_ROLE_ARN = config.get("IAM_ROLE","ARN")
S3_META_DATA = config.get("S3", "META_DATA")
S3_DMG_DATA = config.get("S3", "DMG_DATA")
S3_KILL_DATA = config.get("S3", "KILL_DATA")

class StagingQueries:

    copy_staging_meta = ("""
        COPY staging_meta
        FROM {}
        ACCESS_KEY_ID '{}'
        SECRET_ACCESS_KEY '{}'
        region '{}' 
        FORMAT AS CSV
        IGNOREHEADER 1;
    """).format(S3_META_DATA, ACCESS_KEY_ID, SECRET_ACCESS_KEY, DWH_REGION)

    copy_staging_dmg = ("""
        COPY staging_dmg
        FROM {}
        ACCESS_KEY_ID '{}'
        SECRET_ACCESS_KEY '{}'
        region '{}'
        FORMAT AS CSV
        IGNOREHEADER 1;
    """).format(S3_DMG_DATA, ACCESS_KEY_ID, SECRET_ACCESS_KEY, DWH_REGION)

    copy_staging_kills = ("""
        COPY staging_kills
        FROM {}
        ACCESS_KEY_ID '{}'
        SECRET_ACCESS_KEY '{}'
        region '{}'
        FORMAT AS CSV
        IGNOREHEADER 1;
    """).format(S3_KILL_DATA, ACCESS_KEY_ID, SECRET_ACCESS_KEY, DWH_REGION)

    insert_matches = ("""
        INSERT INTO matches (
        SELECT DISTINCT file AS match_id
        FROM staging_meta
        )
    """)

    insert_teams = ("""
        INSERT INTO teams (
        SELECT
            CONCAT(file, winner_team),
            winner_team
        FROM staging_meta
        )
    """)

    insert_maps = ("""
        INSERT INTO maps (map_name)
        SELECT DISTINCT map
        FROM staging_meta
    """)

    insert_rounds = ("""
        INSERT INTO rounds (
        SELECT
            sm.file,
            CONCAT(sm.file, sm.round),
            sm.round,
            sm.round_type,
            sm.ct_eq_val,
            sm.t_eq_val,
            sm.start_seconds,
            sm.end_seconds,
            sm.winner_team,
            sm.winner_side,
            maps.map_id,
            kills.kills
        FROM staging_meta sm
        LEFT JOIN maps
        ON maps.map_name = sm.map
        LEFT JOIN (
            SELECT file, round, COUNT(*) AS kills
            FROM staging_kills
            GROUP BY file, round
        ) kills
        ON kills.file = sm.file
            AND kills.round = sm.round
        LEFT JOIN (
            SELECT
                file, round,
                SUM(hp_dmg) AS total_hp_dmg,
                SUM(arm_dmg) AS total_arm_dmg
            FROM staging_dmg
            GROUP BY file, round
        ) dmg
        ON dmg.file = sm.file
            AND dmg.round = sm.round
        )
    """)