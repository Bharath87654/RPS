class Scoreboard:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.total_games = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def update(self, winner):
        if winner == "Player":
            self.player_score += 1
            self.wins += 1
        elif winner == "Computer":
            self.computer_score += 1
            self.losses += 1
        elif winner == "Draw":
            self.draws += 1

        if winner != "None":
            self.total_games += 1

    @property
    def win_percentage(self):
        if self.total_games == 0:
            return 0.0
        return round((self.wins / self.total_games) * 100, 1)

    def reset_session(self):
        self.player_score = 0
        self.computer_score = 0

    def reset_all(self):
        self.reset_session()
        self.total_games = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0