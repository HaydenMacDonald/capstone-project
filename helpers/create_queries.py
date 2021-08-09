class CreateQueries:

    create_rounds = ("""
    CREATE TABLE public.rounds (
        match_id varchar(50) NOT NULL,
        round_id varchar(50) NOT NULL,
        round_no int4 NOT NULL,
        round_type varchar(50),
        economy_ct int4 NOT NULL,
        economy_t int4 NOT NULL,
        start_seconds numeric(18,0) NOT NULL,
        end_seconds numeric(18,0) NOT NULL,
        winner_team varchar(50) NOT NULL,
        winner_side varchar(50) NOT NULL,
        map_id int4 NOT NULL,
        bomb_planted BOOLEAN,
        kills int4,
        CONSTRAINT rounds_pkey PRIMARY KEY (round_id)
    );
    """)

    create_matches = ("""
    CREATE TABLE public.matches (
        match_id varchar(50) NOT NULL,
        winner_team varchar(50) NOT NULL,
        loser_team varchar(50) NOT NULL
        CONSTRAINT matches_pkey PRIMARY KEY (match_id)
    );
    """)

    create_teams = ("""
    CREATE TABLE public.teams (
        team_id varchar(50) NOT NULL,
        team_name varchar(50) NOT NULL,
        CONSTRAINT teams_pkey PRIMARY KEY (team_id)
    );
    """)

    create_maps = ("""
    CREATE TABLE public.maps (
        map_id SERIAL PRIMARY KEY,
        map_name varchar (50)
    );
    """)

    create_staging_meta = ("""
    CREATE TABLE public.staging_meta (
        file varchar(50) NOT NULL,
        map varchar(50) NOT NULL,
        round int4 NOT NULL,
        start_seconds numeric(18,0) NOT NULL,
        end_seconds numeric(18,0) NOT NULL,
        winner_team varchar(50) NOT NULL,
        winner_side varchar(50) NOT NULL,
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
        seconds numeric(18,0) NOT NULL,
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
        att_id int4,
        att_rank int4,
        vic_id int4,
        vic_rank int4,
        att_pos_x numeric(18,0),
        att_pos_y numeric(18,0),
        vic_pos_x numeric(18,0),
        vic_pos_y numeric(18,0)
    );
    """)

    create_staging_kills = ("""
    CREATE TABLE public.staging_dmg (
        file varchar(50) NOT NULL,
        round int4 NOT NULL,
        tick int4 NOT NULL,
        seconds numeric(18,0) NOT NULL,
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