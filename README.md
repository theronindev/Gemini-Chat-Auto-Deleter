# Gemini Chat Bulk Deleter

A Python-based automation utility designed to efficiently clear chat history from the Google Gemini interface. This tool utilizes GUI automation to simulate human interaction, allowing for the sequential deletion of chats without manual repetition.

## 📋 Features

* **Interactive Calibration:** Includes a built-in "Teaching Mode" to capture screen coordinates, ensuring compatibility across different screen resolutions and browser layouts.
* **Safety Mechanisms:** Equipped with a "Panic Switch" (`ESC`) for immediate termination and a graceful stop command (`Q`).
* **Human-Like Behavior:** Implements randomized delay intervals to mimic natural mouse movement and avoid bot detection logic.
* **Auto-Scroll:** Automatically scrolls the chat list to ensure continuous operation.

## 🛠 Prerequisites

* **Python 3.x**
* **Operating System:** Windows, macOS, or Linux.
    * *Note:* Linux and macOS users may need to grant Accessibility/Input Monitoring permissions to their terminal. Windows users generally require running the terminal as Administrator due to the `keyboard` library dependency.
* **Browser:** A Chromium-based browser (Chrome, Brave, Edge) is recommended.

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/REPO_NAME.git](https://github.com/YOUR_USERNAME/REPO_NAME.git)
    cd REPO_NAME
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

### Phase 1: Calibration (First Run)
Upon the first execution, the script will enter **Teaching Mode**. You will need to define four coordinate points on your screen.

1.  Run the script:
    ```bash
    python delete.py
    ```
2.  Follow the on-screen prompts. Hover your mouse over the specific UI element and press **`F`** to save the location:
    * **Position 1:** The chat row (hover area).
    * **Position 2:** The "Three Dots" (⋮) menu icon.
    * **Position 3:** The "Delete" option in the dropdown menu.
    * **Position 4:** The "Delete" confirmation button in the modal.

*These positions are saved to `positions.json` for future runs.*

### Phase 2: Execution
Once calibrated, the script will proceed to the deletion loop:

1.  The script initiates a 5-second countdown.
2.  Switch immediately to your browser window.
3.  The script will cycle through the delete process automatically.

## 🎮 Controls

| Key | Function |
| :--- | :--- |
| **F** | **Set Position** (Only in Teaching Mode). |
| **Q** | **Stop:** Finishes the current deletion cycle and exits gracefully. |
| **ESC** | **Panic:** Instantly terminates the script process. |

## ⚠️ Disclaimer

This software uses `pyautogui` to control the mouse and keyboard. 
* **User Responsibility:** Ensure the correct window is in focus before the countdown ends.
* **Liability:** The author is not responsible for accidental data loss or unintended interactions caused by the automation. Use with caution.

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/)