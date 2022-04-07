from application import salary
from application.db import people

if __name__ == '__main__':
    people.get_employees()
    salary.calculate_salary()