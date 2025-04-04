class BaseModel:

    #Létre hozza az adott modelt , táblát az adatbázisban
    @classmethod
    def create_table(cls, db_service):
        try:
            db_service.execute_query(cls.CREATE_TABLE_QUERY)
            print(f"{cls.TABLE_NAME} tábla létrehozva")
        except Exception as e:
            print(f"Hiba a {cls.TABLE_NAME} tábla létrehozásakor: {e}")
            raise

    # Új rekordok beszúrása az adott táblába
    @classmethod
    def insert_data(cls, db_service, values):
        try:
            result = db_service.execute_query(cls.INSERT_QUERY, values, fetch_one=True)
            if not result:
                result = cls._get_existing_id(db_service, values)
            return result
        except Exception as e:
            print(f" Hiba adat beszúrásakor ({cls.TABLE_NAME}): {e}")
            raise

    # Lekérdezi a létező rekordok id-ját az adott táblából
    @classmethod
    def _get_existing_id(cls, db_service, values):
        query = f"""
        SELECT {cls.ID_COLUMN} 
        FROM {cls.TABLE_NAME} 
        WHERE {cls.LOOKUP_COLUMN} = %s;
        """
        return db_service.execute_query(query, (values[0],), fetch_one=True)
