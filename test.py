"""
import sqlite3 # importing sqlite3


conn = sqlite3.connect('test.db')

c = conn.cursor()

# Create table
#c.execute(''' CREATE TABLE dwarak(id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)''')

#insert data
#c.execute("insert into dwarak values (1,'dwarak')")
#c.execute("insert into dwarak values (2,'dwarak')")
#c.execute("insert into dwarak values (3,'prasad')")
#c.execute("insert into dwarak values (4,'sandeep')")
#c.execute("insert into dwarak values (6,'dwarak')")
for row in (c.execute('select * from dwarak')):
    print(row)


conn.commit()
conn.close()

"""
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"
)
"""
import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1', database='mydb',
                              auth_plugin='mysql_native_password')

#print(mydb)