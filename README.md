# 📋 CBSE Result Auto-Checker

> Automated CBSE Class 10 result monitor running on Android via Termux. Sends native notifications when results go live.

---

## 🔍 How It Works

```
Script → Fetches CBSE website → Scans for keywords → Notifies you
```

Runs a loop every 5 minutes, downloads the CBSE results page, and searches for result-related keywords. The moment results are detected — you get a notification instantly.

---

## 📱 Requirements

| Requirement | Source |
|---|---|
| Android Phone | — |
| Termux | [F-Droid](https://f-droid.org) *(not Play Store)* |
| Termux:API | [F-Droid](https://f-droid.org) |
| Python 3 | via Termux |

---

## ⚙️ Installation

### 1. Setup Termux

```bash
pkg update && pkg upgrade -y
pkg install python termux-api -y
pip install requests beautifulsoup4
```

### 2. Clone the Repo

```bash
pkg install git -y
git clone https://github.com/ssannssarr/cbse-result-checker.git
cd cbse-result-checker
```

### 3. Allow Termux Notifications

```
Android Settings → Apps → Termux → Notifications → Allow
Android Settings → Apps → Termux → Battery → Unrestricted
```

---

## 🚀 Usage

```bash
python checker.py
```

### Run in Background (Recommended)

```bash
pkg install screen -y
screen -S cbse
python checker.py

# Detach: Ctrl+A then D
# Reattach later:
screen -r cbse
```

---

## 🔧 Configuration

Open `checker.py` and edit the config block at the top:

```python
# ── CONFIG ──────────────────────────────────────
CHECK_URLS = [
    "https://cbseresults.nic.in",
    "https://results.cbse.nic.in",
    "https://www.cbse.gov.in"
]
KEYWORDS   = ["class x", "class 10", "secondary", "result 2026"]
CHECK_INTERVAL = 300  # seconds — don't go below 60
# ────────────────────────────────────────────────
```

| Variable | Default | Description |
|---|---|---|
| `CHECK_URLS` | 3 CBSE URLs | Sites to monitor |
| `KEYWORDS` | 4 keywords | Trigger words to detect |
| `CHECK_INTERVAL` | `300` (5 min) | Time between checks |

---

## 📲 Notification Methods

### Method 1 — Termux Notification *(Default)*
Native Android notification with sound and vibration. Requires Termux:API app.

### Method 2 — Telegram Bot *(Optional, Recommended)*
More reliable. Works even if Termux is restricted by battery saver.

1. Open Telegram → search `@BotFather` → create a bot → copy token
2. Get your Chat ID from `@userinfobot`
3. Add to `checker.py`:

```python
BOT_TOKEN = "your_bot_token_here"
CHAT_ID   = "your_chat_id_here"

def telegram_notify(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})
```

4. Call `telegram_notify("CBSE Result is LIVE!")` inside the `if found:` block.

---

## 📁 Project Structure

```
cbse-result-checker/
├── checker.py      # Main script
├── README.md       # This file
└── requirements.txt
```

---

## 📦 requirements.txt

```
requests
beautifulsoup4
```

Install via:
```bash
pip install -r requirements.txt
```

---

## ⚠️ Notes

- Do **not** set `CHECK_INTERVAL` below `60` seconds — risk of IP rate-limiting by CBSE servers
- Keep phone **plugged in** or set Termux battery to **Unrestricted**
- CBSE sometimes updates one domain before others — monitoring all 3 URLs is recommended
- Script stops automatically after first detection. Remove the `break` to keep it running.

---

## 🛠️ Built With

- Python 3
- [Requests](https://pypi.org/project/requests/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- Termux + Termux:API

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 👤 Author

**Your Name**
- GitHub: [@ssannssarr](https://github.com/YOUR_USERNAME)
## 🤖 Credits

Coding assistance by [Claude Sonnet 4.6](https://claude.ai) — AI by Anthropic.

---

> ⭐ Star this repo if it helped you catch your results on time!
