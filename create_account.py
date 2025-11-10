import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",      
    password="",
    database="banking_system"
)
cur= mydb.cursor()

sql="""CREATE TABLE accounts(
    account_number INT PRIMARY KEY,
    name VARCHAR(255),
    phone INT(15),
    balance FLOAT DEFAULT 0
    )"""

cur.execute(sql)
mydb.commit()
    