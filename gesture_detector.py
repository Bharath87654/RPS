import cv2
import mediapipe as mp


class GestureDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_draw = mp.solutions.drawing_utils

    def detect_gesture(self, frame):
        """
        Processes the frame, draws landmarks, and returns the recognized gesture.
        Gestures: "Rock", "Paper", "Scissors", or "Unknown"
        """
        # Convert BGR to RGB for MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)
        gesture = "Unknown"

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw landmarks natively on the frame
                self.mp_draw.draw_landmarks(
                    frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                )

                # Analyze landmarks
                gesture = self._analyze_landmarks(hand_landmarks.landmark)

        return gesture, frame

    def _analyze_landmarks(self, landmarks):
        """
        Rule-based gesture recognition using landmark y-coordinates.
        Note: In MediaPipe, the Y-axis decreases going UP the screen.
        """
        # Tip landmarks: Thumb(4), Index(8), Middle(12), Ring(16), Pinky(20)
        # We compare finger tips to their respective PIP/MCP joints to see if they are extended.

        index_open = landmarks[8].y < landmarks[6].y
        middle_open = landmarks[12].y < landmarks[10].y
        ring_open = landmarks[16].y < landmarks[14].y
        pinky_open = landmarks[20].y < landmarks[18].y

        # Simple thumb detection (Checking horizontal distance relative to index MCP)
        # Assumes a right hand facing the camera or left hand back-facing.
        thumb_open = abs(landmarks[4].x - landmarks[5].x) > 0.05

        # 1. Paper: All major fingers are extended
        if index_open and middle_open and ring_open and pinky_open:
            return "Paper"

        # 2. Scissors: Only Index and Middle are extended
        elif index_open and middle_open and not ring_open and not pinky_open:
            return "Scissors"

        # 3. Rock: All major fingers are closed/fisted
        elif not index_open and not middle_open and not ring_open and not pinky_open:
            return "Rock"

        return "Unknown"