Features

Generate passwords of weak, normal, or strong strength

Weak → 6 letters

Normal → 10 letters + digits

Strong → 14 letters + digits + punctuation

Automatic saving of generated passwords to a text file with timestamp

Easy exit from the program

Fully modular (main.py, logic.py, storage.py)

password-generator/
│
├─ main.py        # Program entry point, handles user loop
├─ logic.py       # Contains choose_strength() and generate_password() functions
├─ storage.py     # Functions to save and read passwords from passwords.txt
└─ passwords.txt  # Generated passwords are saved here with timestamps

Notes

All passwords are saved with a timestamp for reference.

Modular structure makes it easy to expand (e.g., add viewing saved passwords, batch generation, et
