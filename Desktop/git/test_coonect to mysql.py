""""
import mysql.connector

mydb = mysql.connector.connect(
  host="pdbmbook.com",
  user="db2022_01",
  password="6368b59bf17be"
)

print(mydb)
"""
from mysql.connector import (connection)

cnx = connection.MySQLConnection( host="pdbmbook.com",
  user="db2022_01",
  password="6368b59bf17be",
                                 database="db2022_01")
cursor = cnx.cursor()

query = "SELECT * from users"
cursor.execute(query)
records=cursor.fetchall()
for i in records:
      print(i) 
cursor.close()
cnx.close()