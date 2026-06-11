import random

class GameLogic:
    def __init__(self, target_wins=3):
        self.target_wins = target_wins  # Best of 5 means first to 3 wins
        self.choices = ["Rock", "Paper", "Scissors"]
        self.difficulty = "Medium" # Placeholder for extension: Easy, Medium, Hard

    def get_computer_move(self, player_history=None):
        """Generates computer move based on current difficulty settings."""
        if self.difficulty == "Easy" and player_history:
            # Predictable or losing behavior could be injected here
            pass
        return random.choice(self.choices)

    def determine_winner(self, player_move, computer_move):
        """
        Returns: 'Player', 'Computer', or 'Draw'
        """
        if player_move == computer_move:
            return "Draw"

        winning_combos = {
            "Rock": "Scissors",
            "Paper": "Rock",
            "Scissors": "Paper"
        }

        if winning_combos[player_move] == computer_move:
            return "Player"
        else:
            return "Computer"