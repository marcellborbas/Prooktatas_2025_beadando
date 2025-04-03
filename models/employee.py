from models.base_model import BaseModel

class Employee(BaseModel):
    TABLE_NAME = "hr.employees"
    ID_COLUMN = "employee_id"

    CREATE_TABLE_QUERY = f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            {ID_COLUMN} SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            department_id INTEGER REFERENCES hr.departments(department_id),
            job_id INTEGER REFERENCES hr.jobs(job_id),
            location_id INTEGER REFERENCES hr.locations(location_id), 
            hire_date DATE NOT NULL,
            salary_id INTEGER REFERENCES hr.salaries(salary_id),
            absence_days INTEGER NOT NULL,
            
            UNIQUE(first_name, last_name, hire_date)
        );
    """

    INSERT_QUERY = f"""
        INSERT INTO {TABLE_NAME} (first_name, last_name, department_id, job_id, location_id, hire_date, salary_id, absence_days)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (first_name, last_name, hire_date) DO NOTHING
        RETURNING {ID_COLUMN};
    """
