import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="world"
)

cursor = conn.cursor()
cursor.execute("SELECT Name, Population FROM country LIMIT 5")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()




