import json
import sqlite3
from klasa import KontoBankowe

nazwa_bazy = "bank.db"

def polacz_baze():
    conn = sqlite3.connect(nazwa_bazy)
    return conn

def utworz_tabele():
    conn = polacz_baze()
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

def dodaj_konto_do_bazy(konto):
    conn = polacz_baze()
    cursor = conn.cursor()

    historia_json = json.dumps(konto.historia, ensure_ascii=False)

    cursor.execute("""
        INSERT INTO konta (wlasciciel, saldo, historia)
        VALUES (?, ?, ?) 
    """, (
        konto.wlasciciel,
        konto.saldo,
        historia_json
    ))
    
    konto.id = cursor.lastrowid

    conn.commit()
    conn.close()
        
def aktualizuj_konto(konto):
    conn = polacz_baze()
    cursor = conn.cursor()

    historia_json = json.dumps(konto.historia, ensure_ascii=False)

    cursor.execute("""
        UPDATE konta
        SET saldo = ?, historia = ?
        WHERE id = ?
    """, (
        konto.saldo,
        historia_json,
        konto.id
    ))

    conn.commit()
    conn.close()

def aktualizuj_przelew(konto_nadawcy, konto_odbiorcy):
    conn = polacz_baze()
    cursor = conn.cursor()

    historia_nadawcy_json = json.dumps(konto_nadawcy.historia, ensure_ascii=False)

    historia_odbiorcy_json = json.dumps(konto_odbiorcy.historia, ensure_ascii=False)

    try:
        cursor.execute("""
            UPDATE konta
            SET saldo = ?, historia = ?
            WHERE id = ?
        """, (
            konto_nadawcy.saldo,
            historia_nadawcy_json,
            konto_nadawcy.id
        ))

        cursor.execute("""
            UPDATE konta
            SET saldo = ?, historia = ?
            WHERE id = ?
        """, (
            konto_odbiorcy.saldo,
            historia_odbiorcy_json,
            konto_odbiorcy.id
        ))

        conn.commit()

    except sqlite3.Error as blad:
        conn.rollback()
        print("Błąd zapisu przelewu:", blad)

    finally:
        conn.close()


def usun_konto_z_bazy(id_konta):
    conn = polacz_baze()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM konta
        WHERE id = ?
    """, (
        id_konta,
    ))

    usunieto = cursor.rowcount > 0

    conn.commit()
    conn.close()

    return usunieto


def wczytaj_z_bazy():
    utworz_tabele()

    conn = polacz_baze()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, wlasciciel, saldo, historia
        FROM konta
        ORDER BY id
    """)

    dane = cursor.fetchall()

    conn.close()

    konta = []

    for element in dane:
        id_konta = element[0]
        wlasciciel = element[1]
        saldo = element[2]
        historia_json = element[3]

        konto = KontoBankowe(wlasciciel, saldo, id_konta)

        if historia_json:
            konto.historia = json.loads(historia_json)
        else:
            konto.historia = []

        konta.append(konto)

    return konta
