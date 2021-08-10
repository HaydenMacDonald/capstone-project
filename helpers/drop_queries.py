class DropQueries:
    drop_staging_meta = "DROP TABLE IF EXISTS staging_meta;"
    drop_staging_dmg = "DROP TABLE IF EXISTS staging_dmg;"
    drop_staging_kills = "DROP TABLE IF EXISTS staging_kills;"
    drop_rounds = "DROP TABLE IF EXISTS rounds;"
    drop_matches = "DROP TABLE IF EXISTS matches;"
    drop_maps = "DROP TABLE IF EXISTS maps;"
    drop_teams = "DROP TABLE IF EXISTS teams;"