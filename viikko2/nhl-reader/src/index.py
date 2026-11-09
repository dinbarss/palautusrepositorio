import re

from rich.console import Console
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats


def _read_season():
    season = input("Season (e.g. 2024-25): ").strip()
    if not re.fullmatch(r"\d{4}-\d{2}", season):
        raise ValueError("Season must use the format YYYY-YY.")
    return season


def _read_nationality():
    nationality = input("Nationality code (e.g. FIN): ").strip().upper()
    if not re.fullmatch(r"[A-Z]{3}", nationality):
        raise ValueError("Nationality must be a three-letter country code.")
    return nationality


def _display_players(players, nationality, season):
    table = Table(title=f"Players from {nationality} ({season})")
    table.add_column("Player")
    table.add_column("Team")
    table.add_column("GP", justify="right")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", justify="right", style="bold")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.games),
            str(player.goals),
            str(player.assists),
            str(player.points),
        )

    Console().print(table)


def main():
    season = _read_season()
    nationality = _read_nationality()
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url))
    players = stats.top_scorers_by_nationality(nationality)
    _display_players(players, nationality, season)


if __name__ == "__main__":
    main()
