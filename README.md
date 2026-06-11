# 🤖 AI-Powered Rock-Paper-Scissors Game

A professional desktop-grade **Rock-Paper-Scissors** game that combines **Computer Vision**, **MediaPipe Hand Tracking**, **OpenCV**, and **Pygame** to create an interactive real-time gaming experience.

Unlike traditional computer vision demos, this project is built as a complete desktop application with a state-driven architecture, responsive UI, score tracking, audio feedback, and tournament management.

---

## 🚀 Features

### 🎯 Real-Time Hand Gesture Recognition

* Uses **Google MediaPipe Hands** to detect and track 21 hand landmarks.
* Captures gestures directly from the webcam.
* Supports:

  * ✊ Rock
  * ✋ Paper
  * ✌️ Scissors

### ⚡ Rule-Based Gesture Detection

* No heavy machine learning models required.
* Fast and lightweight geometric analysis of finger positions.
* Low latency and efficient performance.

### 🎮 State-Driven Game Engine

Smooth game flow using a dedicated state machine:

```text
Start Screen
      ↓
Countdown
      ↓
Gesture Capture
      ↓
Result Evaluation
      ↓
Score Update
      ↓
Next Round / Game Over
```

### 🎨 Modern Desktop UI

* Dark mode interface
* Animated buttons
* Dynamic HUD
* Real-time score updates
* Responsive layout

### 🏆 Tournament Mode

* Best-of-5 gameplay
* Win/Loss tracking
* Match statistics
* Persistent scoreboard
* Performance analytics

### 🔊 Audio & Visual Feedback

* Countdown sounds
* Click effects
* Win/Loss fanfares
* Smooth visual transitions

---

# 📂 Project Structure

```text
ai_rps_game/
│
├── assets/
│   ├── images/       # Game icons and backgrounds
│   ├── sounds/       # Sound effects
│   └── fonts/        # Custom fonts
│
├── gesture_detector.py
│   ├── MediaPipe hand tracking
│   └── Gesture recognition engine
│
├── game_logic.py
│   ├── AI move generation
│   └── Winner evaluation system
│
├── scoreboard.py
│   ├── Match statistics
│   └── Tournament tracking
│
├── ui.py
│   ├── Buttons
│   ├── HUD rendering
│   └── Window management
│
├── main.py
│   └── Application entry point
│
├── requirements.txt
└── README.md
```

---

# 🛠️ Technologies Used

| Technology | Purpose              |
| ---------- | -------------------- |
| Python     | Core Programming     |
| OpenCV     | Webcam Processing    |
| MediaPipe  | Hand Tracking        |
| Pygame     | Desktop Game Engine  |
| NumPy      | Numerical Operations |
| OOP        | Modular Architecture |

---

# 📦 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/ai-rock-paper-scissors.git

cd ai-rock-paper-scissors
```

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv venv

source venv/bin/activate
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Run Application

```bash
python main.py
```

---

# 📐 Gesture Detection Algorithm

The system avoids computationally expensive deep-learning classifiers and instead evaluates finger positions using MediaPipe landmark coordinates.

A finger is considered **extended** if:

```math
Y(TIP) < Y(PIP)
```

where:

* TIP = Finger tip landmark
* PIP = Proximal interphalangeal joint
* Smaller Y value indicates a higher position in the frame

### Gesture Mapping

#### ✊ Rock

```text
All fingers folded
```

#### ✌️ Scissors

```text
Index and Middle fingers extended
Others folded
```

#### ✋ Paper

```text
All fingers extended
```

---

# 🧠 System Workflow

```text
Webcam Feed
      ↓
OpenCV Frame Capture
      ↓
MediaPipe Landmark Detection
      ↓
Finger State Analysis
      ↓
Gesture Classification
      ↓
Game Logic Evaluation
      ↓
UI Rendering & Score Update
```

---

# 🛡️ Build Standalone Executable

## Windows

```bash
pyinstaller --onefile --windowed --add-data "assets;assets" main.py
```

## macOS

```bash
pyinstaller --onefile --windowed --add-data "assets:assets" main.py
```

Compiled files will be generated inside:

```text
dist/
```

Users can run the application without installing Python.

---

# 📊 Future Enhancements

* Multiplayer Mode
* Online Matchmaking
* Hand Gesture Calibration
* Difficulty Levels
* Global Leaderboard
* AI Opponent Learning
* Voice Commands
* Mobile Version

---

# 📸 Screenshots

Add screenshots here:

```text
assets/screenshots/home.png
assets/screenshots/gameplay.png
assets/screenshots/results.png
```

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Bharath Kumar**

If you found this project useful, consider giving it a ⭐ on GitHub!
