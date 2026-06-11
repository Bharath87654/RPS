import cv2
import mediapipe as mp
import os
import sys

# --- CRITICAL PYINSTALLER MEDIAPIPE COMPATIBILITY PATCH ---
# This forces MediaPipe's underlying C++ modules to look into the
# true runtime directory where PyInstaller extracted the tracking models.
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    mediapipe_dir = os.path.join(sys._MEIPASS, 'mediapipe')
    # Force rewrite the module's absolute file path bindings
    mp.solutions.hands.HAND_CONNECTIONS = mp.solutions.hands.HAND_CONNECTIONS
    os.environ["MEDIAPIPE_BINARY_LOGDIR"] = sys._MEIPASS


# ----------------------------------------------------------

class GestureDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands

        # Initialize natively
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.5,  # Kept low for lighting flexibility
            min_tracking_confidence=0.5
        )
        self.mp_draw = mp.solutions.drawing_utils

    def detect_gesture(self, frame):
        """Processes the frame and returns the recognized gesture."""
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)
        gesture = "Unknown"

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(
                    frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                )
                gesture = self._analyze_landmarks(hand_landmarks.landmark)

        return gesture, frame

    def _analyze_landmarks(self, landmarks):
        # Keep your exact landmark mathematical checking system here...
        index_open = landmarks[8].y < landmarks[6].y
        middle_open = landmarks[12].y < landmarks[10].y
        ring_open = landmarks[16].y < landmarks[14].y
        pinky_open = landmarks[20].y < landmarks[18].y

        if index_open and middle_open and ring_open and pinky_open:
            return "Paper"
        elif index_open and middle_open and not ring_open and not pinky_open:
            return "Scissors"
        elif not index_open and not middle_open and not ring_open and not pinky_open:
            return "Rock"
        return "Unknown"