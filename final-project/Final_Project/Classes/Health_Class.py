from Final_Project.Classes import User_Class
from datetime import date
class Health(User_Class.User):
    def __init__(self,f_name,l_name,age,weight,height_feet,height_inches,Calories_In, Calories_Out):
        super().__init__(f_name,l_name,age,weight,height_feet,height_inches)
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.height_feet = height_feet
        self.height_inches = height_inches
        self.Calories_In = Calories_In
        self.Calories_Out = Calories_Out


    @property
    def Calories_In(self):
        return self._Calories_In

    @Calories_In.setter
    def Calories_In(self,value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Enter Correct Calories Intake")
        else:
            self._Calories_In = value

    @property
    def Calories_Out(self):
        return self._Calories_Out

    @Calories_Out.setter
    def Calories_Out(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Enter Correct Calories Burned")
        else:
            self._Calories_Out = value


    def height(self):
        return "{}FT, {}IN".format(self._height_feet, self._height_inches)

    def bmi(self):
        if self.height_inches > 0 and self.height_feet > 0 and self.weight > 0:
            try:
                inches = self.height_feet * 12 + self.height_inches
                self.bmi = self.weight / (inches * inches) * 703
                BMI = round(self.bmi, 1)
                return BMI
            except ValueError:
                raise ValueError("Incorrect info can't calculate BMI.")

    def current_info(self):
        return "Date: {}".format(date.today()) + "\n" + "Name: {},{}".format(self.f_name,self.l_name) +  "\n" + "Height: {}".format(self.height())\
    + "\n" "Age: {}".format(self.age) + "\n" + "Weight: {}Lbs".format(self.weight) + "\n"\
               + "Calories Intake: {}".format(self.Calories_In) + "\n" + \
               "Calories Burned: {}".format(self.Calories_Out) + "\n" "Current BMI: {}".format(self.bmi())

    def current_date(self):
        date.today()













