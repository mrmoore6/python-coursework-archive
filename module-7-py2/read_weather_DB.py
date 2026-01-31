import pandas as pd
import Weather_Data as wd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('weather_data.db')
c = conn.cursor()
data = wd.weather_data

data = data.to_sql("Precipitation",conn, if_exists='replace', index=False)

conn.execute('''  
SELECT * FROM Precipitation
          ''')

state_data = wd.state_county_df
state_data = state_data.to_sql("Location", conn, if_exists='replace', index=False)

conn.execute('''  
SELECT * FROM Location
          ''')


for row in c.fetchall():
    print(row)

weather_data_df = pd.read_sql_query("SELECT * FROM Precipitation", sqlite3.connect('weather_data.db'))

print(weather_data_df)
weather_data_df = weather_data_df.sort_values(by='PRCP', ascending=True)
print(weather_data_df)
labels= ["RAIN/ICE", "SNOW"]
plt.pie(weather_data_df['precip_type'].value_counts(), labels=labels)
plt.show()
conn.commit()
conn.close()