class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()

        nationality_players = filter(
            lambda player: player.nationality == nationality, players)

        sorted_players = sorted(
            nationality_players, key=lambda player: player.goals + player.assists, reverse=True)

        return sorted_players

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa."""
        players = self.reader.get_players()

        sorted_players = sorted(
            players, key=lambda player: player.goals, reverse=True)

        return sorted_players[:how_many]

    def top_scorers_by_team(self, team):
        """Palauttaa joukkueen pelaajat pisteiden mukaan laskevassa järjestyksessä."""
        players = self.reader.get_players()

        team_players = filter(lambda player: player.team == team, players)

        sorted_players = sorted(
            team_players, key=lambda player: player.goals + player.assists, reverse=True)

        return sorted_players