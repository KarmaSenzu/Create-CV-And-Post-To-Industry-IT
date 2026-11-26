# AGY Job Hunter & CV Commander

Multi-profile web dashboard and CLI workflow for managing job applications and generating tailored CVs with RenderCV.

## Setup on a New Device

1. Clone this repository:
   ```bash
   git clone https://github.com/KarmaSenzu/Create-CV-And-Post-To-Industry-IT.git
   cd Create-CV-And-Post-To-Industry-IT
   ```

2. Create a Python virtual environment and install dependencies:
   ```bash
   python3 -m venv .venv
   .venv/bin/pip install -r requirements.txt
   ```

3. Start the web server:
   - **macOS / Linux:**
     ```bash
     ./start_server.sh
     ```
   - **Or directly with Python (macOS / Linux / Windows):**
     ```bash
     .venv/bin/python server.py
     ```
     (On Windows: `.venv\Scripts\python.exe server.py`)

4. Open `http://localhost:8080` in your browser.

