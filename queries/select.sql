"""
1.	Melyik részlegben dolgozik a legtöbb munkavállaló?
"""

SELECT d.department_name, COUNT(e.employee_id) AS employee_count
FROM hr.employees e
JOIN hr.departments d ON e.department_id = d.department_id
GROUP BY d.department_name
HAVING COUNT(e.employee_id) = (
    SELECT MAX(employee_count)
    FROM (
        SELECT COUNT(e.employee_id) AS employee_count
        FROM hr.employees e
        GROUP BY e.department_id
    ) AS dept_counts
);

"""
2.	Kik azok a dolgozók, akik 2023-ban legalább 10 nap szabadságot vettek ki?
"""

SELECT e.first_name, e.last_name, e.hire_date, e.absence_days
FROM hr.employees e
WHERE EXTRACT(YEAR FROM e.hire_date) = 2023
AND e.absence_days >= 10;

"""
3.	Részlegek szerinti átlagfizetések kiszámítása
"""
SELECT department_name, AVG(monthly_salary) AS average_salary
FROM hr.employees e
JOIN hr.departments d ON e.department_id = d.department_id
JOIN hr.salaries s ON e.salary_id = s.salary_id
GROUP BY department_name;

"""
4.	Melyik városban dolgozik a legtöbb különböző munkakörű dolgozó?
"""

SELECT l.city, COUNT(DISTINCT e.job_id) AS job_count
FROM hr.employees e
JOIN hr.locations l ON e.location_id = l.location_id
GROUP BY l.city
HAVING COUNT(DISTINCT e.job_id) = (
    SELECT MAX(job_count)
    FROM (
        SELECT COUNT(DISTINCT e.job_id) AS job_count
        FROM hr.employees e
        JOIN hr.locations l ON e.location_id = l.location_id
        GROUP BY l.city
    ) AS city_counts
);


"""
5.	Dolgozók listája, akik 2023-ban csatlakoztak a céghez, beosztásukkal és részlegükkel együtt
"""
SELECT e.first_name, e.last_name, e.hire_date, j.job_title, d.department_name
FROM hr.employees e
JOIN hr.jobs j ON e.job_id = j.job_id
JOIN hr.departments d ON e.department_id = d.department_id
WHERE EXTRACT(YEAR FROM e.hire_date) = 2023;