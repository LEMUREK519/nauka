import json
import sqlite3
from klasa import KontoBankowe

nazwa_bazy = "bank.db"

def utworz_tabele():
    conn = sqlite3.connect(nazwa_bazy)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS konta (
            id INTEGER PRIMARY KEY,
            wlasciciel TEXT NOT NULL,
            saldo REAL NOT NULL,
            historia TEXT NOT NULL
            )
        """)
    
    conn.commit()
    conn.close()

def zapisz_do_bazy(konta):
    conn = sqlite3.connect(nazwa_bazy)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM konta")

    for konto in konta:
        historia_json = json.dumps(konto.historia, ensure_ascii=False)
        
        cursor.execute("""
            INSERT INTO konta (wlasciciel, saldo, historia)
            VALUES (?, ?, ?) 
        """, (
            konto.wlasciciel,
            konto.saldo,
            historia_json
        ))
    
    conn.commit()
    conn.close()
        
def wczytaj_z_bazy():
    utworz_tabele()

    conn = sqlite3.connect(nazwa_bazy)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT wlasciciel, saldo, historia 
                   FROM konta 
                   ORDER BY id
    """)

    dane = cursor.fetchall()

    conn.close()

    konta = []

    for element in dane:
        wlasciciel = element[0]
        saldo = element[1]
        historia_json = element[2]

        konto = KontoBankowe(wlasciciel, saldo)

        if historia_json:
            konto.historia = json.loads(historia_json)
        else:
            konto.historia = []

        konta.append(konto)

    return konta