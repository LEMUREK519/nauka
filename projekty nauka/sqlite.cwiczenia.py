import sqlite3

conn = sqlite3.connect("test_bank.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS konta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    wlasciciel TEXT NOT NULL,
    saldo REAL NOT NULL
)
""")

cursor.execute(
    "INSERT INTO konta (wlasciciel, saldo) VALUES (?, ?)",
    ("Julia", 5000)
)

cursor.execute(
    "INSERT INTO konta (wlasciciel, saldo) VALUES (?, ?)",
    ("Kacper", 3000)
)

conn.commit()

cursor.execute("SELECT * FROM konta")
konta = cursor.fetchall()

print("Lista kont:")
for konto in konta:
    print(konto)

conn.close()