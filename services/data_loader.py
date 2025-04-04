import csv
from models import Department, Job, Location, Salary, Employee

class DataLoader:

    def __init__(self, db_service):
        self.db_service = db_service

    # Összes szükséges tábla létrehozása
    def create_tables(self):
        for model in [Department, Job, Location, Salary, Employee]:
            model.create_table(self.db_service)

    # csv betöltése és feldolgozása
    def load_data_from_csv(self, file_path):
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                department_id = Department.insert_data(self.db_service, (row['department'],))
                job_id = Job.insert_data(self.db_service, (row['job'],))
                location_id = Location.insert_data(self.db_service, (row['location'],))
                salary_id = Salary.insert_data(self.db_service, (int(row['monthly_salary']),))

                if None in (department_id, job_id, location_id, salary_id):
                    print(f"HIBA: Hiányzó érték beszúrásnál: {row}")
                    continue

                self.insert_employee(row, department_id[0], job_id[0], location_id[0], salary_id[0])

    def insert_employee(self, row, department_id, job_id, location_id, salary_id):
        query = f"""
        INSERT INTO {Employee.TABLE_NAME} (
            first_name, last_name, department_id, job_id, 
            location_id, hire_date, salary_id, absence_days
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (first_name, last_name, hire_date) DO NOTHING;
        """
        params = (
            row['first_name'], row['last_name'], department_id, job_id,
            location_id, row['hire_date'], salary_id, int(row['absence_days'])
        )

        self.db_service.execute_query(query, params)
