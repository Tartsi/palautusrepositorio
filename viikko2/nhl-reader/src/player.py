class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']

    def get_points(self):
        return self.goals + self.assists

    def __str__(self):

        return f"{self.name:20}{self.team}  {self.goals} + {self.assists} = {self.get_points()}"