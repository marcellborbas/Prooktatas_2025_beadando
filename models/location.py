from models.base_model import BaseModel

class Location(BaseModel):
    TABLE_NAME = "hr.locations"
    ID_COLUMN = "location_id"
    LOOKUP_COLUMN = "city"

    # Tábla létrehozása ha az még nem létezik
    CREATE_TABLE_QUERY = f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            {ID_COLUMN} SERIAL PRIMARY KEY,
            {LOOKUP_COLUMN} VARCHAR(50) UNIQUE NOT NULL
        );
    """

    # Az új helyszínek beszúrása
    INSERT_QUERY = f"""
        INSERT INTO {TABLE_NAME} ({LOOKUP_COLUMN})
        VALUES (%s)
        ON CONFLICT ({LOOKUP_COLUMN}) DO NOTHING
        RETURNING {ID_COLUMN};
    """
