import psycopg2
from config.database import DATABASE_CONFIG

def test_database_connection():
    try:
        conn = psycopg2.connect(**DATABASE_CONFIG)
        conn.autocommit = True

        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            db_version = cur.fetchone()
            print(f"Sikeres kapcsolat! A Postgersql verzió: {db_version[0]}")

            cur.execute("SELECT EXISTS(SELECT 1 FROM information_schema.schemata WHERE schema_name = 'hr');")
            hr_schema_exists = cur.fetchone()[0]
            print(f"A 'hr' SCHEMA létezik: {'Igen!' if hr_schema_exists else 'Nem!'}")
        return True
    
    except psycopg2.OperationalError as e: 
        print(f"Hiba történt a kapcsolat létrehozásakor: {e}")
        print("\nGyakori okok:")
        print("- Hibás adatbázis név, felhasználónév vagy jelszó")
        print("- A PostgreSQL szerver nem fut")
        print("- Hálózati probléma")
        print("- A config/database_config.py nem megfelelő")
        return False
    
    finally:
        if 'conn' in locals():
            conn.close()
            print("A kapcsolat lezárva!")

if __name__ == '__main__':
    print("Adatbázis kapcsolat tesztelése...")
    if test_database_connection():
        print("\n Minden renden, lehet az adatbázissal kapcsolódni")
    else:
        print("\nHiba történt az adatbázishoz kapcsolódás során!")
