class CreateQueries:

    create_rounds = ("""
    CREATE TABLE public.rounds (
        match_id varchar(50) NOT NULL,
        round_id varchar(50) PRIMARY KEY,
        round_no int4 NOT NULL,
        round_type varchar(50),
        economy_ct int4 NOT NULL,
        economy_t int4 NOT NULL,
        start_seconds numeric(18,0),
        end_seconds numeric(18,0),
        winner_team varchar(50),
        winner_side varchar(50),
        map_id int4 NOT NULL,
        bomb_planted BOOLEAN,
        kills int4
    );
    """)

    create_matches = ("""
    CREATE TABLE public.matches (
        match_id varchar(50) PRIMARY KEY,
        winner_team varchar(50),
        loser_team varchar(50)
    );
    """)

    create_teams = ("""
    CREATE TABLE public.teams (
        team_id varchar(50) PRIMARY KEY,
        team_name varchar(50) NOT NULL
    );
    """)

    create_maps = ("""
    CREATE TABLE public.maps (
        map_id int4 IDENTITY(1, 1) PRIMARY KEY,
        map_name varchar (50)
    );
    """)

    create_staging_meta = ("""
    CREATE TABLE public.staging_meta (
        file varchar(50) NOT NULL,
        map varchar(50) NOT NULL,
        round int4 NOT NULL,
        start_seconds numeric(18,0),
        end_seconds numeric(18,0),
        winner_team varchar(50),
        winner_side varchar(50),
        round_type varchar(50),
        ct_eq_val int4 NOT NULL,
        t_eq_val int4 NOT NULL
    );
    """)

    create_staging_dmg = ("""
    CREATE TABLE public.staging_dmg (
        file varchar(50) NOT NULL,
        round int4 NOT NULL,
        tick int4 NOT NULL,
        seconds numeric(18,0),
        att_team varchar(50) NOT NULL,
        vic_team varchar(50) NOT NULL,
        att_side varchar(50),
        vic_side varchar(50),
        hp_dmg int4,
        arm_dmg int4,
        is_bomb_planted BOOLEAN,
        bomb_site varchar(2),
        hitbox varchar(50),
        wp varchar(50),
        wp_type varchar(50),
        att_id bigint,
        att_rank int4,
        vic_id bigint,
        vic_rank int4,
        att_pos_x numeric(18,0),
        att_pos_y numeric(18,0),
        vic_pos_x numeric(18,0),
        vic_pos_y numeric(18,0)
    );
    """)

    create_staging_kills = ("""
    CREATE TABLE public.staging_kills (
        file varchar(50) NOT NULL,
        round int4 NOT NULL,
        tick int4 NOT NULL,
        seconds numeric(18,0),
        att_team varchar(50) NOT NULL,
        vic_team varchar(50) NOT NULL,
        att_side varchar(50),
        vic_side varchar(50),
        wp varchar(50),
        wp_type varchar(50),
        ct_alive int4 NOT NULL,
        t_alive int4 NOT NULL,
        is_bomb_planted BOOLEAN
    );
    """)