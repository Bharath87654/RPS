import pygame
import cv2
import sys
import time
from gesture_detector import GestureDetector
from game_logic import GameLogic
from scoreboard import Scoreboard
from ui import UI, Button


class GameEngine:
    def __init__(self):
        self.ui = UI()
        self.detector = GestureDetector()
        self.game_logic = GameLogic(target_wins=3)
        self.scoreboard = Scoreboard()

        # State Management: 'START', 'PLAYING', 'ROUND_OVER', 'GAME_OVER'
        self.state = 'START'
        self.clock = pygame.time.Clock()

        # Video Capture Setup
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Critical Error: Webcam not accessible.")
            sys.exit()

        # Phase Parameters
        self.countdown_start_time = None
        self.current_countdown = 3
        self.player_final_gesture = "Unknown"
        self.computer_final_move = "None"
        self.round_winner = "None"

        # UI Buttons
        self.btn_start = Button(412, 400, 200, 60, "START", self.ui.COLOR_PRIMARY, self.ui.COLOR_ACCENT,
                                self.ui.font_body)
        self.btn_restart = Button(412, 500, 200, 60, "PLAY AGAIN", self.ui.COLOR_PRIMARY, self.ui.COLOR_ACCENT,
                                  self.ui.font_body)

    def run(self):
        while True:
            self.ui.draw_background()
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self._cleanup()

            # State Routing Machine
            if self.state == 'START':
                self._handle_start_screen(events)
            elif self.state == 'PLAYING':
                self._handle_playing_screen(events)
            elif self.state == 'ROUND_OVER':
                self._handle_round_over(events)
            elif self.state == 'GAME_OVER':
                self._handle_game_over(events)

            pygame.display.flip()
            self.clock.tick(30)

    def _handle_start_screen(self, events):
        self.ui.draw_text("AI Rock Paper Scissors", self.ui.font_title, (255, 255, 255), self.ui.width // 2, 200,
                          center=True)
        self.btn_start.draw(self.ui.screen)

        for event in events:
            if self.btn_start.is_clicked(event):
                self.state = 'PLAYING'
                self.countdown_start_time = time.time()
                self.current_countdown = 3

    def _handle_playing_screen(self, events):
        ret, frame = self.cap.read()
        if not ret:
            return

        frame = cv2.flip(frame, 1)  # Mirror display
        gesture, frame = self.detector.detect_gesture(frame)

        # Blit Webcam Output onto Pygame Screen Canvas
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (480, 360))
        surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        self.ui.screen.blit(surface, (40, 150))

        # Display Live Tracked Gesture Status
        self.ui.draw_text(f"Detected: {gesture}", self.ui.font_body, self.ui.COLOR_ACCENT, 40, 530)

        # Display Match Standings Dashboard
        self._draw_hud()

        # Handle the dynamic timer mechanics
        elapsed = time.time() - self.countdown_start_time
        if elapsed < 3.0:
            self.current_countdown = 3 - int(elapsed)
            self.ui.draw_text(str(self.current_countdown), self.ui.font_title, (255, 69, 0), 740, 300, center=True)
        elif elapsed < 4.0:
            self.ui.draw_text("SHOW!", self.ui.font_title, (0, 255, 0), 740, 300, center=True)
            # Freeze gesture state exactly at target frame threshold
            if gesture != "Unknown":
                self.player_final_gesture = gesture
        else:
            # Evaluate current loop outcome
            if self.player_final_gesture == "Unknown":
                # Fallback mechanism if no hand was visible or clear
                self.player_final_gesture = "Rock"

            self.computer_final_move = self.game_logic.get_computer_move()
            self.round_winner = self.game_logic.determine_winner(self.player_final_gesture, self.computer_final_move)
            self.scoreboard.update(self.round_winner)

            # Phase evaluation check
            if self.scoreboard.player_score >= self.game_logic.target_wins or self.scoreboard.computer_score >= self.game_logic.target_wins:
                self.state = 'GAME_OVER'
            else:
                self.state = 'ROUND_OVER'
                self.countdown_start_time = time.time()  # Re-use timer frame tracking

    def _handle_round_over(self, events):
        # Render static historical frame placeholders
        self.ui.draw_text(f"Player Used: {self.player_final_gesture}", self.ui.font_body, (255, 255, 255), 200, 200)
        self.ui.draw_text(f"Computer Used: {self.computer_final_move}", self.ui.font_body, (255, 255, 255), 600, 200)

        color = (0, 255, 0) if self.round_winner == "Player" else (255, 0, 0) if self.round_winner == "Computer" else (
            255, 255, 0)
        self.ui.draw_text(f"Outcome: {self.round_winner}", self.ui.font_title, color, self.ui.width // 2, 350,
                          center=True)

        self._draw_hud()

        # Give player a 3-second window to digest performance metrics before reloading loop automation
        if time.time() - self.countdown_start_time > 3.0:
            self.player_final_gesture = "Unknown"
            self.state = 'PLAYING'
            self.countdown_start_time = time.time()

    def _handle_game_over(self, events):
        match_winner = "Player Wins the Match!" if self.scoreboard.player_score >= self.game_logic.target_wins else "Computer Wins the Match!"
        self.ui.draw_text(match_winner, self.ui.font_title, self.ui.COLOR_ACCENT, self.ui.width // 2, 200, center=True)

        # Display aggregate analytics tracking variables
        self.ui.draw_text(f"Total Matches Played: {self.scoreboard.total_games}", self.ui.font_body, (255, 255, 255),
                          self.ui.width // 2, 300, center=True)
        self.ui.draw_text(f"Win Rate Accuracy: {self.scoreboard.win_percentage}%", self.ui.font_body, (255, 255, 255),
                          self.ui.width // 2, 350, center=True)

        self.btn_restart.draw(self.ui.screen)
        for event in events:
            if self.btn_restart.is_clicked(event):
                self.scoreboard.reset_all()
                self.state = 'PLAYING'
                self.countdown_start_time = time.time()

    def _draw_hud(self):
        # Draw Score HUD bounding components
        pygame.draw.rect(self.ui.screen, self.ui.COLOR_PANEL, (560, 480, 420, 200), border_radius=8)
        self.ui.draw_text(f"Player Score: {self.scoreboard.player_score}", self.ui.font_score, (255, 255, 255), 590,
                          510)
        self.ui.draw_text(f"Comp Score: {self.scoreboard.computer_score}", self.ui.font_score, (255, 255, 255), 590,
                          590)

    def _cleanup(self):
        self.cap.release()
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    game = GameEngine()
    game.run()