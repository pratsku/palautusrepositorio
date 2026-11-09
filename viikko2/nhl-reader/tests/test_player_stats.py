from types import SimpleNamespace

from player_stats import PlayerStats


class StubPlayerReader:
    def __init__(self, players):
        self.players = players

    def get_players(self):
        return self.players


def create_player(name, team, goals, assists, nationality="FIN"):
    return SimpleNamespace(
        name=name,
        team=team,
        goals=goals,
        assists=assists,
        nationality=nationality,
    )


def test_top_goal_scorers_returns_requested_number_in_goal_order():
    players = [
        create_player("A", "DAL", 10, 1),
        create_player("B", "DAL", 20, 2),
        create_player("C", "CAR", 15, 3),
    ]

    stats = PlayerStats(StubPlayerReader(players))

    result = stats.top_goal_scorers(2)

    assert [player.name for player in result] == ["B", "C"]


def test_top_scorers_by_team_returns_only_team_players_in_points_order():
    players = [
        create_player("A", "DAL", 10, 5),
        create_player("B", "DAL", 12, 4),
        create_player("C", "CAR", 30, 30),
        create_player("D", "DAL", 5, 2),
    ]

    stats = PlayerStats(StubPlayerReader(players))

    result = stats.top_scorers_by_team("DAL")

    assert [player.name for player in result] == ["B", "A", "D"]


def test_top_scorers_by_team_returns_empty_list_for_unknown_team():
    stats = PlayerStats(StubPlayerReader([]))

    assert stats.top_scorers_by_team("XXX") == []
