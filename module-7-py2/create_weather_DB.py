import sqlite3
from sqlite3 import Error


def db_conn(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error:
        print(Error)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


db = "weather_data.db"

create_weather_precipitation_table = """ CREATE TABLE IF NOT EXISTS Precipitation(
                                            date text,
                                            precipitation float,
                                            precip_type text,
                                            county text,
                                            FOREIGN KEY(county) REFERENCES Location(county)
                                            
                                    ); """

create_weather_location_table = """CREATE TABLE IF NOT EXISTS Location(
                                    county text PRIMARY KEY,
                                    state text
                                );"""


conn = db_conn(db)

if conn is not None:
    create_table(conn, create_weather_location_table)

    create_table(conn, create_weather_precipitation_table)
else:
    print("Error! cannot create the database connection.")

cur = conn.cursor()

result = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
table_names = sorted(list(zip(*result))[0])
print("\ntables are:" + '\n' + '\n'.join(table_names))

for table_name in table_names:
    result = cur.execute("PRAGMA table_info('%s')" % table_name).fetchall()
    column_names = list(zip(*result))[1]
    print(("\ncolumn names for %s:" % table_name)
          + '\n'
          + ('\n'.join(column_names)))

