from player import Player


class PlayerStats:

    def __init__(self, reader):
        self.reader = reader

    def get_top_scorers_by_nationality(self, nationality):

        players = self.reader.get_players()
        top_scorers = []

        for player in players:

            if player.nationality == nationality:
                top_scorers.append(player)

        return sorted(top_scorers, key=Player.get_points, reverse=True)
