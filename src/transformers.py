# src/transformers.py

def top_5_players(df, categories):
    """
    Given a DataFrame and a list of statistical categories, return the top 5 players
    per category.
    """
    result = {}
    for cat in categories:
        if cat not in df.columns:
            continue
        # Sort descending and take top 5
        top_players = df.sort_values(by=cat, ascending=False).head(5)
        result[cat] = top_players.to_dict(orient='records')
    return result

def add_betting_advice(top_players_dict):
    """
    Add simple betting advice to top players.
    For demo purposes, we just add a confidence score based on stat rank.
    """
    advice_dict = {}
    for cat, players in top_players_dict.items():
        advised_players = []
        for i, player in enumerate(players):
            stat_value = player.get(cat, 0)
            # Simple recommendation logic
            recommendation = "OVER" if stat_value >= 20 else "UNDER"
            confidence = "HIGH" if i == 0 else "MEDIUM" if i <= 2 else "LOW"

            player_copy = player.copy()
            player_copy.update({
                'category': cat,
                'recommendation': recommendation,
                'confidence': confidence
            })
            advised_players.append(player_copy)
        advice_dict[cat] = advised_players
    return advice_dict
