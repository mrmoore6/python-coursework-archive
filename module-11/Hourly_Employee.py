"""
Michael Moore
11/9/20
uses employee as a base class to make hourly employee.
"""

from Employee_2 import employee
from datetime import date

class hourly_employee(employee):
    def __init__(self,last_name,first_name,start_date, hourly_pay):
        super().__init__(last_name,first_name)
        self.start_date = start_date
        self.hourly_pay = hourly_pay

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
    def hourly_pay(self):
        return self._hourly_pay

    @hourly_pay.setter
    def hourly_pay(self,value):
        if not isinstance(value, float):
            raise ValueError
        else:
            self._hourly_pay = value

    def give_raise(self, value):
        if value <= self.hourly_pay:
            raise ValueError
        else:
            self._hourly_pay = value
            print("\n"+"Hourly pay changed to ${}".format(value) +
                  '\n')

    def display(self):
        return "Hourly Employee \n{}".format(employee.display_name(self)) + "\n" + "Start Date: {}".format(self.start_date) + "\n" + \
               "Hourly Pay: ${}".format(self.hourly_pay)


try:
    mike = hourly_employee("Moore","Mike",date(2001,12,20),10.00)
    print(mike.display())
    mike.give_raise(12.00)
    print(mike.display())
except ValueError:
    raise ValueError
