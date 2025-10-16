import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FOLDER = BASE_DIR / "data"
DATA_FILE = DATA_FOLDER / "users.json"

def check_dataset_exists():
    DATA_FOLDER.mkdir(exist_ok=True)  # creates folder if not exists
    if not DATA_FILE.exists():
        # Initialize file with empty structure
        with open(DATA_FILE, "w") as f:
            json.dump({"data": []}, f, indent=2)

def read_usersdata():
    check_dataset_exists()
    with open(DATA_FILE, "r") as f:
        users = json.load(f)
    return users

def add_userdata(user: dict):
    users = read_usersdata()
    if "data" not in users:
        users["data"] = []
    users["data"].append(user)
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=2)
