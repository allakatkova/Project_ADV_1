import application.salary as salary
import application.db.people as people
import datetime
from stringcolor import *

if __name__ == '__main__':

    salary.calculate_salary()
    people.get_employees()
    print()
    today = datetime.datetime.now().date()
    print(cs(str(today), "DeepPink3", "lightgrey6").bold())
