from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats


def main():
    console = Console()

    season = Prompt.ask("Season", default="2024-25")
    team = Prompt.ask("Team", default="DAL")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    players = stats.top_scorers_by_team(team)

    table = Table(title=f"Players from {team}")

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