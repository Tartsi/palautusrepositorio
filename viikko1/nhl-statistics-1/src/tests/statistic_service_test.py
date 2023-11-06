import unittest
from statistics_service import SortBy, StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]
    
class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_player_list_is_correct_length(self):
        self.assertEqual(len(self.stats._players), 5)

    def test_search_returns_correct_player(self):
        player = self.stats.search("Semenko")
        self.assertEqual(player.name, "Semenko")
    
    def test_search_returns_none_for_missing_players(self):
        player = self.stats.search("McDavid")
        self.assertIsNone(player)

    def test_team_returns_correct_players(self):
        team_players = self.stats.team("EDM")
        
        self.assertEqual(len(team_players), 3)

        self.assertEqual(team_players[0].name, "Semenko")
        self.assertEqual(team_players[1].name, "Kurri")
        self.assertEqual(team_players[2].name, "Gretzky")

    def test_top_returns_correct_number_of_players(self):
        top_players = self.stats.top(2)
        self.assertEqual(len(top_players), 3)
    
    def test_top_returns_correct_order_of_players_points(self):
        top_players = self.stats.top(4)
        expected = ["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"]
        actual = [player.name for player in top_players]
        self.assertEqual(actual, expected)
    
    def test_top_returns_correct_order_of_players_goals(self):
        top_goalscorers = self.stats.top(4, sort_by=SortBy.GOALS)
        expected = ["Lemieux", "Yzerman", "Kurri", "Gretzky", "Semenko"]
        actual = [player.name for player in top_goalscorers]
        self.assertEqual(actual, expected)
           
    def test_top_returns_correct_order_of_players_assists(self):
        top_assisters = self.stats.top(4, sort_by=SortBy.ASSISTS)
        expected = ["Gretzky", "Yzerman", "Lemieux", "Kurri", "Semenko"]
        actual = [player.name for player in top_assisters]
        self.assertEqual(actual, expected)