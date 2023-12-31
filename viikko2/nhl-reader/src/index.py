from player_reader import PlayerReader
from player_stats import PlayerStats
from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.get_top_scorers_by_nationality("RUS")

    for player in players:
        print(player)


if __name__ == "__main__":
    main()
