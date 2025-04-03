import sys
import os
from services.db_service import DatabaseService
from services.data_loader import DataLoader

def main():
    try:
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        db_service = DatabaseService()
        data_loader = DataLoader(db_service)
        print("\n Táblák létrehozása...")

        data_loader.create_tables()
        print("\n Adatok betöltése...")

        data_loader.load_data_from_csv('data/Denormaliz_lt_HR_adatok.csv')
        print("\n Minden művelet sikeresen befejeződött!")

    except Exception as e:
        print(f"\n Váratlan hiba: {e}")

    finally:
         if 'db_service' in locals():
            db_service.close()

if __name__ == "__main__":
    main()
