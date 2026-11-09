from player_reader import PlayerReader
from player_stats import PlayerStats

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt


def main():
    console = Console()

    season = Prompt.ask("Season", default="2024-25")
    nationality = Prompt.ask("Nationality", default="FIN")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    players = stats.top_scorers_by_nationality(nationality)

    table = Table(title=f"Players from {nationality}")

    table.add_column("Name", style="cyan")
    table.add_column("Team", style="magenta")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", justify="right", style="green")

    for player in players:
        points = player.goals + player.assists

        table.add_row(
            player.name,
            str(player.team),
            str(player.goals),
            str(player.assists),
            str(points))

    console.print(table)


if __name__ == "__main__":
    main()