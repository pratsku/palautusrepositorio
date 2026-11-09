class Player:
    def __init__(self, player):
        self.name = player["name"]
        self.nationality = player["nationality"]
        self.team = player["team"]
        self.goals = player["goals"]
        self.assists = player["assists"]

    def __str__(self):
        return f"{self.name:20} {self.team:3} {self.goals:2} + {self.assists:2} = {self.goals + self.assists}"