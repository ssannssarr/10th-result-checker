import requests
from bs4 import BeautifulSoup
import time
import subprocess
import os

# ── CONFIG ──────────────────────────────────────
CHECK_URL = "https://cbseresults.nic.in" and "https://results.cbse.nic.in/"
KEYWORDS = ["class x", "class 10", "result 2026" 
]
CHECK_INTERVAL = 300  # seconds (5 minutes)
# ────────────────────────────────────────────────

def notify(title, message):
    subprocess.run([
        "termux-notification",
        "--title", title,
        "--content", message,
        "--sound",
        "--vibrate", "500,100,500"
    ])

def check_result():
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(CHECK_URL, headers=headers, timeout=10)
        page_text = response.text.lower()
        soup = BeautifulSoup(page_text, "html.parser")

        for keyword in KEYWORDS:
            if keyword in page_text:
                notify(
                    "✅ CBSE Result LIVE!",
                    f"Keyword '{keyword}' detected on {CHECK_URL}"
                )
                print(f"[FOUND] '{keyword}' detected!")
                return True

        print(f"[{time.strftime('%H:%M:%S')}] Not live yet...")
        return False

    except Exception as e:
        print(f"[ERROR] {e}")
        return False

# ── MAIN LOOP ────────────────────────────────────
print("Checker started. Press Ctrl+C to stop.\n")
while True:
    found = check_result()
    if found:
        break  # Stop after first detection (remove to keep checking)
    time.sleep(CHECK_INTERVAL)
