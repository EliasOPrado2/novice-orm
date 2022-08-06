from base import BaseModel
from manager import BaseManager


class Employee(BaseModel):
    manager_class = BaseManager
    table_name = "employees"


# Example of SIMPLE implementation:

# SQL: SELECT salary, grade FROM employees;
employees = Employee.objects.select(
    "salary", "grade"
)  # employees: List[Employee]

# SQL: INSERT INTO employees (first_name, last_name, salary)
#  	VALUES ('Yan', 'KIKI', 10000), ('Yoweri', 'ALOH', 15000);

employees_data = [
    {"first_name": "Yan", "last_name": "KIKI", "salary": 10000},
    {"first_name": "Yoweri", "last_name": "ALOH", "salary": 15000},
]
Employee.objects.bulk_insert(rows=employees_data)

# SQL: UPDATE employees SET salary = 17000, grade = 'L2';
Employee.objects.update(new_data={"salary": 17000, "grade": "L2"})

# SQL: DELETE FROM employees;
Employee.objects.delete()
