from Final_Project.DB import Final_DB as db
import tkinter
import sqlite3
from Final_Project.Classes import Health_Class as h



conn = sqlite3.connect('health_log.db')
c = conn.cursor()



class Final_Gui:
    def __init__(self,master):
        master.title("Mike's Health App")
        master.geometry("500x500")
        # GUI
        self.welcome = tkinter.Label(master,text = "Welcome")
        self.welcome.config(font=('Courier','44'))
        # -------
        self.add_log_button = tkinter.Button(master, text="Add Log", command=lambda: self.add_log())
        self.view_average = tkinter.Button(master, text="Veiw Avg", command=lambda: self.average())
        self.display_button = tkinter.Button(master, text="Display Logs", command=lambda: self.display_log())
        self.restart_button = tkinter.Button(master, text="Restart Log", command=lambda: self.restart_log())
        self.exit_log = tkinter.Button(master, text="Exit", command=lambda: self.exit())
        # -------
        self.firstname_label = tkinter.Label(text= "Enter First Name")
        self.lastname_label = tkinter.Label(text="Enter Last Name")
        self.age_label = tkinter.Label(text="Enter Age")
        self.weight_label = tkinter.Label(text="Enter Weight in LBS")
        self.height_ft_label = tkinter.Label(text="Enter Height Feet")
        self.height_in_label = tkinter.Label(text="Enter Height Inches")
        self.calories_in_label = tkinter.Label(text="Enter Calories Consumed")
        self.calories_out_label = tkinter.Label(text="Enter Calories Burned")
        self.view = tkinter.Label(master, text="Test")
        # -------
        self.f_name = tkinter.Entry(master)
        self.l_name = tkinter.Entry(master)
        self.age = tkinter.Entry(master)
        self.weight = tkinter.Entry(master)
        self.height_in = tkinter.Entry(master)
        self.height_ft = tkinter.Entry(master)
        self.calories_in = tkinter.Entry(master)
        self.calories_out =  tkinter.Entry(master)
        # -------
        self.welcome.pack()
        self.firstname_label.pack()
        self.f_name.pack()
        self.lastname_label.pack()
        self.l_name.pack()
        # -------
        self.age_label.pack()
        self.age.pack()
        # -------
        self.weight_label.pack()
        self.weight.pack()
        self.height_ft_label.pack()
        self.height_ft.pack()
        self.height_in_label.pack()
        self.height_in.pack()
        # -------
        self.calories_in_label.pack()
        self.calories_in.pack()
        self.calories_out_label.pack()
        self.calories_out.pack()
        # -------
        self.add_log_button.pack()
        self.display_button.pack()
        self.view_average.pack()
        self.exit_log.pack()
        self.view.pack()
        self.restart_button.pack(side='bottom')



    def add_log(self):
        c.execute("""CREATE TABLE IF NOT EXISTS Health(
               Log_date text,
               First_NAME text,
               Last_NAME text,
               weight REAL,
               calories_in REAl,
               calories_out REAl,
               bmi REAL
        )""")
        user = h.Health(self.f_name.get(),self.l_name.get(),int(self.age.get()),
        float(self.weight.get()),int(self.height_ft.get()),int(self.height_in.get()),int(self.calories_out.get()),int(self.calories_in.get()))
        db.insert_log(user)
        db.conn.commit()

        self.add_log_button.configure(state=tkinter.DISABLED)
        self.view_average.configure(state=tkinter.NORMAL)

    def display_log(self):
      rows = db.display()
      text = ""
      rows.insert(0,("Date","Name","Weight","Calorie Intake","Calories Burned","BMI"))
      rows.insert(0,'Health Log')
      for row in rows:
        text += str(row)
        text += "\n"
        self.view.configure(text=text)



    def average(self):
        with conn:
            c.execute("SELECT ROUND(avg(bmi), 2) FROM Health")
            a = c.fetchall()
            a = str(a[0])[1:-2]
            c.execute("SELECT ROUND(avg(weight), 2) FROM Health")
            b = c.fetchall()
            b = str(b[0])[1:-2]
            c.execute("SELECT ROUND(avg(calories_in), 2) FROM Health")
            x = c.fetchall()
            x = str(x[0])[1:-2]
            c.execute("SELECT ROUND(avg(calories_out), 2) FROM Health")
            d = c.fetchall()
            d = str(d[0])[1:-2]
            text = "BMI Average: {}".format(a) + "\n" + "Weight Average: {}LBS".format(b)+  "\n" + \
                   "\n" + 'Average Calories Consumed {}'.format(x) + "\n" + 'Average Calories Burned {}'.format(d)
            self.view.configure(text=text)

    def restart_log(self):
        c.execute("DELETE FROM Health")
        conn.commit()

    def exit(self):
        conn.close()
        exit()

root = tkinter.Tk()
DB = Final_Gui(root)
root.mainloop()
