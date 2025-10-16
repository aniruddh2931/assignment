import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FOLDER = BASE_DIR / "data"
DATA_FOLDER.mkdir(exist_ok=True)

DATA_FILE = DATA_FOLDER / "users.json"
if not DATA_FILE.exists():
    DATA_FILE.write_text('{"data": []}', encoding="utf-8")

def read_usersdata():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def add_userdata(user: dict):
    data = read_usersdata()
    data.setdefault("data", []).append(user)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
