import sqlite3

conn = sqlite3.connect('weather_data2.db')
c = conn.cursor()

c.execute('UPDATE Precipitation SET PRCP=PRCP*25.4')
c.execute('SELECT ROUND(PRCP,2) FROM Precipitation')
c.execute('DELETE FROM Precipitation WHERE PRCP = 391.16')
prcp = conn.execute('SELECT PRCP FROM Precipitation').fetchall()


conn.commit()
conn.close()

print(prcp)


