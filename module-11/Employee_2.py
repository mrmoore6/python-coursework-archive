from datetime import date
class employee:

    def __init__(self,last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name


    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise ValueError
        else:
            self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise ValueError
        else:
            self._first_name = value

    def display_name(self):
        return "{},{}".format(self._first_name, self._last_name)
