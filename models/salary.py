from models.base_model import BaseModel

class Salary(BaseModel):
    TABLE_NAME = "hr.salaries"
    ID_COLUMN = "salary_id"
    LOOKUP_COLUMN = "monthly_salary"

    CREATE_TABLE_QUERY = f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            {ID_COLUMN} SERIAL PRIMARY KEY,
            {LOOKUP_COLUMN} INTEGER NOT NULL,
            UNIQUE({LOOKUP_COLUMN})
        );
    """

    INSERT_QUERY = f"""
        INSERT INTO {TABLE_NAME} ({LOOKUP_COLUMN})
        VALUES (%s)
        ON CONFLICT ({LOOKUP_COLUMN}) DO NOTHING
        RETURNING {ID_COLUMN};
    """
