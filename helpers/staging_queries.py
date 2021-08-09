import configparser

# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')
DWH_REGION = config.get("CLUSTER","REGION")
DWH_IAM_ROLE_ARN = config.get("IAM_ROLE","ARN")
S3_META_DATA = config.get("S3", "META_DATA")
S3_DMG_DATA = config.get("S3", "DMG_DATA")
S3_KILL_DATA = config.get("S3", "KILL_DATA")

class StagingQueries:

    copy_staging_meta = ("""
        COPY staging_meta
        FROM {}
        CREDENTIALS 'aws_iam_role={}'
        region {}
        COMPUPDATE OFF
        DELIMITER ',' 
        CSV HEADER;
    """).format(S3_META_DATA, DWH_IAM_ROLE_ARN, DWH_REGION)

    copy_staging_dmg = ("""
        COPY staging_dmg
        FROM {}
        CREDENTIALS 'aws_iam_role={}'
        region {}
        COMPUPDATE OFF
        DELIMITER ',' 
        CSV HEADER;
    """).format(S3_DMG_DATA, DWH_IAM_ROLE_ARN, DWH_REGION)

    copy_staging_kills = ("""
        COPY staging_kills
        FROM {}
        CREDENTIALS 'aws_iam_role={}'
        region {}
        COMPUPDATE OFF
        DELIMITER ',' 
        CSV HEADER;
    """).format(S3_DMG_DATA, DWH_IAM_ROLE_ARN, DWH_REGION)

    insert_matches = ("""
        INSERT INTO matches VALUES(match_id)
        SELECT DISTINCT file AS match_id
        FROM staging_meta
    """)

    insert_teams = ("""
        INSERT INTO teams VALUES(team_id, team_name)
        SELECT
            CONCAT(file, "-", winner_team),
            winner_team
        FROM staging_meta
    """)

    insert_maps = ("""
        INSERT INTO maps VALUES(map_name)
        SELECT DISTINCT map
        FROM staging_meta
    """)

    insert_rounds = ("""
    SELECT
        sm.file,
        CONCAT(sm.file, "-", sm.round),
        sm.round_no,
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
        SELECT COUNT(*) AS kills
        FROM staging_kills
        GROUP BY file, round
    ) kills
    ON kills.file = sm.file
        AND kills.round = sm.round_no
    LEFT JOIN (
        SELECT 
            SUM(hp_dmg) AS total_hp_dmg,
            SUM(arm_dmg) AS total_arm_dmg
        FROM staging_dmg
        WHERE att_id <> "None"
        GROUP BY file, round
    ) dmg
    ON dmg.file = sm.file
        AND dmg.round = sm.round_no
    """)