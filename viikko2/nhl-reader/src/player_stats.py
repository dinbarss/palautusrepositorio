class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_goal_scorers(self, how_many):
        """Return up to how_many players ordered by goals scored."""
        players = self.reader.get_players()
        return sorted(
            players,
            key=lambda player: player.goals,
            reverse=True,
        )[:how_many]

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        national_players = [
            player for player in players
            if player.nationality == nationality
        ]
        return sorted(
            national_players,
            key=lambda player: player.points,
            reverse=True,
        )

    def top_scorers_by_team(self, team):
        players = self.reader.get_players()
        team_players = [
            player for player in players
            if team in (member.strip() for member in player.team.split(","))
        ]
        return sorted(
            team_players,
            key=lambda player: player.points,
            reverse=True,
        )
