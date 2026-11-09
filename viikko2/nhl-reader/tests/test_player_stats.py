from player import Player
from player_stats import PlayerStats


class StubPlayerReader:
    def __init__(self, players):
        self.players = players

    def get_players(self):
        return self.players


def make_player(name, nationality, team, goals, assists):
    return Player(
        {
            "name": name,
            "nationality": nationality,
            "team": team,
            "goals": goals,
            "assists": assists,
            "games": 10,
            "id": 1,
        }
    )


def test_top_scorers_by_nationality_returns_players_in_points_order():
    players = [
        make_player("Fin One", "FIN", "DAL", 2, 1),
        make_player("Other", "SWE", "DAL", 10, 4),
        make_player("Fin Two", "FIN", "SEA", 1, 3),
    ]
    stats = PlayerStats(StubPlayerReader(players))

    result = stats.top_scorers_by_nationality("FIN")

    assert [player.name for player in result] == ["Fin Two", "Fin One"]


def test_top_scorers_by_team_matches_multi_team_player_and_sorts():
    players = [
        make_player("Lower", "FIN", "DAL", 2, 1),
        make_player("Other", "SWE", "SEA", 10, 4),
        make_player("Higher", "USA", "SEA, DAL", 4, 3),
    ]
    stats = PlayerStats(StubPlayerReader(players))

    result = stats.top_scorers_by_team("DAL")

    assert [player.name for player in result] == ["Higher", "Lower"]
