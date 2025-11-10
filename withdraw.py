import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",      
    password="",
    database="banking_system",
)
cur= mydb.cursor()

acc=int(input("Enter account number: "))
amt=float(input("Enter amount to be withdrawn: "))
sql="SELECT balance FROM accounts WHERE account_number=%s"
val=(acc,)
cur.execute(sql,val)
result=cur.fetchone()
if result:
    a=result[0]
    if a>=amt:
        new_balance=a-amt
        sql="UPDATE accounts SET balance=%s WHERE account_number=%s"
        val=(new_balance,acc)
        cur.execute(sql,val)    
        mydb.commit()
        print(f"\nAmount ₹{amt} withdrawn successfully!")
    else:
        print("\nInsufficient balance!")
        

