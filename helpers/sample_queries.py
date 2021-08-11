class SampleQueries:

    sample_rounds = {'table':'rounds', 'query':"""
        SELECT *
        FROM public.rounds
        LIMIT 10
    """}

    sample_matches = {'table':'matches', 'query':"""
        SELECT *
        FROM public.matches
        LIMIT 10
    """}

    sample_teams = {'table':'teams', 'query':"""
        SELECT *
        FROM public.teams
        LIMIT 10
    """}

    sample_maps = {'table':'maps', 'query':"""
        SELECT *
        FROM maps
        LIMIT 10
    """}