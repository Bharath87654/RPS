🤖 AI-Powered Rock-Paper-Scissors Game
A polished, desktop-grade Rock-Paper-Scissors game featuring real-time, rule-based hand gesture tracking via your webcam. Unlike typical computer vision proofs-of-concept, this application wraps the pipeline inside a state-driven, object-oriented Pygame desktop engine complete with visual animations, audio responses, a match database scoreboard, and persistent tournament structures.

🌟 Key Features
Zero-Lag Hand Recognition: Uses Google MediaPipe Hands framework to isolate hand joints natively.

Geometric Rule Engine: Bypasses bloated neural network model dependencies by evaluating spatial array structures in real time.

State-Driven Game Loop: Features clean screen state synchronization routing (Start Screen → Active Countdown → Freeze Eval → Score Update → Game Over).

Polished Desktop UI: Dark-mode dashboard layout including dynamic HUD rendering, button micro-animations, and responsive score panels.

Tournament Tracker: Automatically logs round metrics, absolute win rates, loss thresholds, and total frame analytics for a Best-of-5 system.

📂 Architecture Structure
The system strictly follows Object-Oriented Programming (OOP) patterns to ensure loose decoupling between computer vision processing elements and drawing canvases:

Plaintext
ai_rps_game/
│
├── assets/
│   ├── images/       # Game icons (rock, paper, scissors) and background canvases
│   ├── sounds/       # Sound effects (beeps, clicks, win/loss fanfares)
│   └── fonts/        # Custom game font (.ttf)
│
├── gesture_detector.py # MediaPipe pipeline wrapper & coordinate analytics
├── game_logic.py       # Computer AI move generation & outcome matrix state machine
├── scoreboard.py       # Metrics engine & lifetime math calculation tracking
├── ui.py               # Reusable button elements and Pygame window setup
├── main.py             # Main pipeline thread coordinator
├── requirements.txt    # Dependency lockfile
└── README.md           # Documentation
🛠️ Installation & Execution
1. Prerequisites
Ensure you have Python 3.10 or newer installed on your native machine along with an operational webcam interface.

2. Clone Repository
Bash
git clone https://github.com/yourusername/ai-rock-paper-scissors.git
cd ai-rock-paper-scissors
3. Initialize Environment
Bash
# Setup clean isolated environment
python -m venv venv

# Activate on Linux/macOS
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate
4. Install Dependencies
Bash
pip install -r requirements.txt
5. Launch App Engine
Bash
python main.py
📐 Algorithmic Tracking Logic
Instead of relying on heavy deep learning dataset models like CNNs, this system optimizes frame efficiency by analyzing the vertical Y-axis values of relative finger tracking points.

Because MediaPipe scales coordinates from top-to-bottom (0.0 at top frame boundary, 1.0 at bottom boundary), checking if a finger is extended is formulated mathematically as:

Is_Extended=Y 
TIP_ID
​
 <Y 
PIP_ID
​
 
Plaintext
       (8) Index Tip             
          |                      Paper: [8, 12, 16, 20] < MCP Joints
       (7) PIP Joint             Scissors: Only [8, 12] < MCP Joints
          |                      Rock: All Tip Y-coords > MCP Joints
       (6) MCP Joint             
🛡️ Desktop Deployment Compilation
To bundle this application into a standalone executable (.exe or .app) so users don't need a Python environment installed, compile using PyInstaller:

Bash
# Windows Compilation
pyinstaller --onefile --windowed --add-data "assets;assets" main.py

# macOS Compilation
pyinstaller --onefile --windowed --add-data "assets:assets" main.py
The output distributable package will generate directly inside the local /dist directory path.

📝 Note: Upon launch, the OS may request webcam permissions. This is required for the application to map local camera matrices into Pygame pixel textures.
