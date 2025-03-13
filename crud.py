import mysql.connector

try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Anand@738',
        database = 'indigo'
    )
    mycursor = conn.cursor()
    print("Connection established")
except:
    print("Connection Error")

# create a database on the db server
# mycursor.execute("CREATE DATABASE indigo")
# conn.commit()


# Create a table
# airport -> airport_id | code| name | city
# mycursor.execute("""
# CREATE TABLE airport(
#     airport_id INTEGER PRIMARY KEY,
#     code VARCHAR(255) NOT NULL,
#     name VARCHAR(255) NOT NULL,
#     city VARCHAR(255) NOT NULL
# )
# """)
# conn.commit()



#  Insert data to the table
# mycursor.execute("""
# INSERT INTO airport VALUES
# (1,'DEL','IGIA','New Delhi'),
# (2,'BOM','CSMA','Mumbai'),
# (3,'STV','SA','Surat')
# """)
# conn.commit()


# search/retrive
mycursor.execute("SELECT * from airport where airport_id>1")
data = mycursor.fetchall()
print(data)

for i in data:
    print(i[3])
    
    
# Update
mycursor.execute("""
UPDATE airport
SET city = 'Bomby'
WHERE airport_id = 2
""")
conn.commit()

mycursor.execute("SELECT * from airport")
data = mycursor.fetchall()
print(data)


# DELETE
mycursor.execute("DELETE FROM airport WHERE airport_id = 3")
conn.commit()

mycursor.execute("SELECT * FROM airport")
data = mycursor.fetchall()
print(data)