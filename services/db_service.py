import psycopg2
from config.database import DATABASE_CONFIG

class DatabaseService:

    def __init__(self):
        self.conn = None
        self.connect()
        self.create_schema()
        self._check_schema_exists()

    # Adatbázis kapcsolat létrehozása
    def connect(self):
        try:
            self.conn = psycopg2.connect(**DATABASE_CONFIG)
            self.conn.autocommit = True
            print("Az adatbázis kapcsolat létrejött")
        except Exception as e:
            print(f"Kapcsolódási hiba: {e}")
            raise

    # hr SCHEMA ellenőrzése
    def _check_schema_exists(self):
        query = """
        SELECT EXISTS(
            SELECT 1 FROM information_schema.schemata 
            WHERE schema_name = 'hr'
        );
        """
        result = self.execute_query(query, fetch_one=True)
        if not result[0]:
            raise RuntimeError("A 'hr' séma nem létezik az adatbázisban!")

    # Ha nem létezik a hr SCHEMA akkor létrehozzuk
    def create_schema(self):
        query = "CREATE SCHEMA IF NOT EXISTS hr;"
        self.execute_query(query)
        print("A 'hr' séma ellenőrizve/létrehozva")

    def execute_query(self, query, params=None, fetch_one=False):
        try:
            with self.conn.cursor() as cur:
                cur.execute(query, params or ())
                if fetch_one:
                    return cur.fetchone()
                return cur.rowcount
        except Exception as e:
            print(f"Lekérdezési hiba: {e}")
            print(f"Vizsgált lekérdezés: {query}")
            raise

    def close(self):
        if self.conn and not self.conn.closed:
            self.conn.close()
            print("A kapcsolat lezárva")
