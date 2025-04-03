from models.base_model import BaseModel

class Job(BaseModel):
    TABLE_NAME = "hr.jobs"
    ID_COLUMN = "job_id"
    LOOKUP_COLUMN = "job_title"
    CREATE_TABLE_QUERY = f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            {ID_COLUMN} SERIAL PRIMARY KEY,
            {LOOKUP_COLUMN} VARCHAR(50) UNIQUE NOT NULL
        );
    """

    INSERT_QUERY = f"""
        INSERT INTO {TABLE_NAME} ({LOOKUP_COLUMN})
        VALUES (%s)
        ON CONFLICT ({LOOKUP_COLUMN}) DO NOTHING
        RETURNING {ID_COLUMN};
    """
