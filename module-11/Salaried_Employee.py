"""
Michael Moore
11/9/20
uses employee as a base class to make salaried employee.
"""

from Employee_2 import employee
from datetime import date

class salaried_employee(employee):
    def __init__(self,last_name,first_name,start_date, salary):
        super().__init__(last_name,first_name)
        self.start_date = start_date
        self.salary = salary

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self,value):
        if not isinstance(value, date):
            raise ValueError
        else:
            self._start_date = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,value):
        if value < 10000:
            raise ValueError("Enter a salary")
        if not isinstance(value, int):
            raise ValueError
        else:
            self._salary = value

    def give_raise(self, value):
        if value <= self.salary:
                raise ValueError
        else:
            self._salary = value
            print("\n" + "Salary pay changed to ${}".format(value) +
                    '\n')

    def display(self):
        return "Salary Employee \n{}".format(employee.display_name(self)) + "\n" + "Start Date: {}".format(
            self.start_date) + "\n" + \
                "Hourly Pay: ${}".format(self.salary)


try:
    jake = salaried_employee("Moore","Jake",date(2000,10,20),40000)
    print(jake.display())
    jake.give_raise(45000)
    print(jake.display())
except ValueError:
    raise ValueError
