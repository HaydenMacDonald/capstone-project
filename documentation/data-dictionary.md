# Data Dictionary

## rounds 
* match_id (varchar) - unique identifier for the match
* round_id (varchar) - unique identifier for the round
* round_no (int4) - the round number
* round_type (varchar) - the round type, based on economy.
* economy_ct (int4) - economy of the Counter Terrorist side.
* economy_t (int4) -  economy of the Terrorist side.
* start_seconds (numeric) - Round start time in seconds 
* end_seconds (numeric) - Round end time in seconds
* winner_team (varchar) - ID of winning team
* winner_side (varchar) - Side of winning team
* map_id (int4) - unique identifier for the map the match was played on
* bomb_planted (BOOLEAN) - indicator of whether the bomb was planted
* kills (int4) - number of kills that occurred in the round

## matches
* match_id (varchar) - unique identifier for the match
* winner_team (varchar) - ID of winning team
* loser_team (varchar) - ID of losing team

## teams
* team_id (varchar) - unique identifier for the team
* team_name (varchar) - the team name

## maps
* map_id (int4) - unique identifier for the map
* map_name (varchar) - the map's name

