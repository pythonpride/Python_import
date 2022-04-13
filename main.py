from application import salary
from application.db import people
import datetime

if __name__ == '__main__':
    now = datetime.datetime.now()
    print(now.strftime("%d-%m-%Y %H:%M"))
    people.get_employees()
    salary.calculate_salary()
