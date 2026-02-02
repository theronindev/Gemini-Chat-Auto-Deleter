import pyautogui
import keyboard
import time
import json
import os
import random
import sys

pyautogui.FAILSAFE = True
POSITIONS_FILE = "positions.json"

def panic():
    """Instant stop if ESC is pressed"""
    if keyboard.is_pressed("esc"):
        print("\n🛑 PANIC STOP (ESC pressed)")
        sys.exit(0)

def human_sleep(a, b):
    """Sleep for a random interval to simulate human behavior"""
    time.sleep(random.uniform(a, b))

def move_smooth(x, y):
    """Move mouse smoothly to target (faster than before)"""
    pyautogui.moveTo(x, y, duration=random.uniform(0.05, 0.08))

def get_location(name):
    """Teach a position by pressing F"""
    print(f"\n👉 {name}")
    print("Move mouse over target and press [F]")
    while True:
        panic()
        if keyboard.is_pressed("f"):
            pos = pyautogui.position()
            print(f"✅ Saved: {pos}")
            time.sleep(0.6)
            return pos

def teach():
    """Teach all 4 positions"""
    print("\n=== TEACHING MODE ===")
    print("Gemini must be open and chat list visible")

    hover = get_location("1/4 — CHAT ROW (hover area, NOT dots)")
    menu  = get_location("2/4 — THREE DOTS (⋮)")
    delete = get_location("3/4 — DELETE option")
    confirm = get_location("4/4 — CONFIRM Delete button")

    data = {
        "hover": hover,
        "menu": menu,
        "delete": delete,
        "confirm": confirm
    }

    with open(POSITIONS_FILE, "w") as f:
        json.dump(data, f)

    print("\n💾 Positions saved")
    return data

def load_positions():
    """Load positions and handle old files"""
    if not os.path.exists(POSITIONS_FILE):
        return teach()

    with open(POSITIONS_FILE) as f:
        data = json.load(f)

    # Backward compatibility check
    required_keys = {"hover", "menu", "delete", "confirm"}
    if not required_keys.issubset(data.keys()):
        print("⚠️ Old positions file detected.")
        print("🔁 Re-teaching positions is required.")
        return teach()

    print("📂 Loaded saved positions")
    return data

def main():
    print("\n=== GEMINI AUTO DELETE (SPEED-OPTIMIZED) ===")
    print("ESC = PANIC | Q = STOP\n")

    pos = load_positions()

    hx, hy = pos["hover"]
    mx, my = pos["menu"]
    dx, dy = pos["delete"]
    cx, cy = pos["confirm"]

    print("Switch to Brave window NOW")
    for i in range(5, 0, -1):
        print(f"Starting in {i}...")
        time.sleep(1)

    count = 0
    print("\n▶ Running...\n")

    while True:
        panic()

        if keyboard.is_pressed("q"):
            print("\n🛑 Stopped by user")
            break

        # 1. Hover chat row (CRITICAL)
        move_smooth(hx, hy)
        human_sleep(0.2, 0.35)

        # 2. Click three dots
        move_smooth(mx, my)
        pyautogui.click()
        human_sleep(0.2, 0.3)

        # 3. Click delete
        move_smooth(dx, dy)
        pyautogui.click()
        human_sleep(0.2, 0.3)

        # 4. Confirm delete
        move_smooth(cx, cy)
        pyautogui.click()
        human_sleep(1.2, 1.5)  # reduced wait for speed

        count += 1
        print(f"🗑️ Deleted chat #{count}")

        # 5. Scroll every 3 deletions to refresh chat list
        if count % 3 == 0:
            pyautogui.scroll(-200)
            human_sleep(0.2, 0.35)

    print(f"\n✅ Finished. Total deleted: {count}")

if __name__ == "__main__":
    main()
