# src/validators.py

def is_valid_player(row):
    """
    Basic validation for NBA player rows.
    - Player name exists
    - Player played at least 10 games (G column)
    """
    try:
        player_name = row.get('Player', '').strip()
        games = int(row.get('G', 0))
        return player_name != '' and games >= 10
    except:
        return False
