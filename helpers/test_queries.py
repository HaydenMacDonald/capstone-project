class TestQueries:
    test_rounds = {'query': "SELECT SUM(CASE WHEN round_id IS NULL THEN 1 ELSE 0 END) AS null_count FROM rounds", 'expected': 0}
    test_matches = {'query': "SELECT SUM(CASE WHEN match_id IS NULL THEN 1 ELSE 0 END) AS null_count FROM matches", 'expected': 0}
    test_teams = {'query': "SELECT SUM(CASE WHEN team_id IS NULL THEN 1 ELSE 0 END) AS null_count FROM teams", 'expected': 0}
    test_maps = {'query': "SELECT SUM(CASE WHEN map_name IS NULL THEN 1 ELSE 0 END) AS null_count FROM maps", 'expected': 0}
