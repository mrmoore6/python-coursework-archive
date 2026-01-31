import sqlite3
from datetime import date


conn = sqlite3.connect('health_log.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS Health(
               Log_date text,
               First_NAME text,
               Last_NAME text,
               weight REAL,
               calories_in REAl,
               calories_out REAl,
               bmi REAL
        )""")

def display():
    c.execute("SELECT * FROM Health")
    return c.fetchall()

def insert_log(user):
    with conn:
        c.execute("INSERT INTO Health VALUES (:Log_Date, :First_NAME,:Last_NAME,:weight,:calories_in,:calories_out,:bmi)",
              {"Log_Date": date.today(),"First_NAME": user.f_name, "Last_NAME":user.l_name,"weight": user.weight,
               "calories_in": user.Calories_In,"calories_out": user.Calories_Out, "bmi": user.bmi()})

def average_bmi():
    with conn:
        c.execute("SELECT ROUND(avg(bmi), 2) FROM Health")
        print(c.fetchall())



#def update_log(user):
    #log_number = 0
   # with conn:
        #c.execute("UPDATE Health SET  = ",
       # {"info": user.current_info()})





c.execute("SELECT * FROM Health WHERE First_NAME = :First_NAME",{'First_NAME': "Mike"})

print(c.fetchall())
print(average_bmi())

