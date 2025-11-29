from datetime import datetime

def save_password(password):
    """Append a password with timestamp to passwords.txt"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{now}] {password}"
    with open("passwords.txt", "a") as f:
        f.write(entry + "\n")
