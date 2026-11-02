import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  # 4+12 = 16
            Player("Lemieux", "PIT", 45, 54),  # 45+54 = 99
            Player("Kurri", "EDM", 37, 53),  # 37+53 = 90
            Player("Yzerman", "DET", 42, 56),  # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def names(self, players):
        return [player.name for player in players]

    def test_search_finds_existing_player(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")

    def test_search_returns_none_for_unknown_player(self):
        player = self.stats.search("Selanne")

        self.assertIsNone(player)

    def test_team_returns_all_players_of_team(self):
        players = self.stats.team("EDM")

        self.assertEqual(self.names(players), ["Semenko", "Kurri", "Gretzky"])

    def test_team_returns_empty_list_for_unknown_team(self):
        players = self.stats.team("XYZ")

        self.assertEqual(players, [])

    def test_top_without_parameter_sorts_by_points(self):
        players = self.stats.top(2)

        self.assertEqual(self.names(players), ["Gretzky", "Lemieux"])

    def test_top_sorts_by_points(self):
        players = self.stats.top(3, SortBy.POINTS)

        self.assertEqual(
            self.names(players), ["Gretzky", "Lemieux", "Yzerman"]
        )

    def test_top_sorts_by_goals(self):
        players = self.stats.top(3, SortBy.GOALS)

        self.assertEqual(
            self.names(players), ["Lemieux", "Yzerman", "Kurri"]
        )

    def test_top_sorts_by_assists(self):
        players = self.stats.top(3, SortBy.ASSISTS)

        self.assertEqual(
            self.names(players), ["Gretzky", "Yzerman", "Lemieux"]
        )
