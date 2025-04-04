from models.base_model import BaseModel

class Department(BaseModel):
    TABLE_NAME = "hr.departments"
    ID_COLUMN = "department_id"
    LOOKUP_COLUMN = "department_name"

    # Tábla létrehozása ha az még nem létezik
    CREATE_TABLE_QUERY = f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            {ID_COLUMN} SERIAL PRIMARY KEY,
            {LOOKUP_COLUMN} VARCHAR(50) UNIQUE NOT NULL
        );
    """

    # Az új osztályok beszúrása
    INSERT_QUERY = f"""
        INSERT INTO {TABLE_NAME} ({LOOKUP_COLUMN})
        VALUES (%s)
        ON CONFLICT ({LOOKUP_COLUMN}) DO NOTHING
        RETURNING {ID_COLUMN};
    """
