import sqlite3

## connect to sqlite
connection = sqlite3.connect("student.db")

## create cursor
cursor = connection.cursor()

## create table
table_info =  """
    CREATE TABLE IF NOT EXISTS STUDENT(NAME VARCHAR(25), 
    CLASS VARCHAR(25),SECTION VARCHAR(25), MARKS INT);
  """

cursor.execute(table_info)


## Insert Some more records
cursor.execute('''INSERT INTO STUDENT VALUES ('Krishi', 'Data Science', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Sudhanshu', 'Data Science', 'B', 100)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Darius', 'Data Science', 'A', 86)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Vikash', 'DEVOPS', 'A', 50)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Dipesh', 'DEVOPS', 'A', 35)''')



# Display all the records
print("all the inserted records are")

data = cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
  print(row)


# Close the connection
connection.commit()

connection.close()

