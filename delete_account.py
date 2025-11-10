import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",      
    password="",
    database="banking_system"
)
cur= mydb.cursor()

acc=int(input("Enter account number to be deleted: "))
sql="DELETE FROM accounts WHERE account_number=%s"
val=(acc,)
cur.execute(sql,val)
mydb.commit()
print(f"\nAccount Number: {acc} deleted successfully!")


