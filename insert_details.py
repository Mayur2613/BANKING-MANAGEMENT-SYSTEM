import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="banking_system"
)

cur = mydb.cursor()

def insert_details():
    acc = int(input("Enter account number: "))
    name = input("Enter name: ")
    phone = int(input("Enter phone number: "))
    balance = float(input("Enter initial balance: "))

    sql = "INSERT INTO accounts (account_number, name, phone, balance) VALUES (%s, %s, %s, %s)"
    val = (acc, name, phone, balance)

    cur.execute(sql, val)
    mydb.commit()

    print(f"\nAccount added successfully for '{name}' with Account Number: {acc}")
    print(f"Current Balance: ₹{balance: }")

insert_details()
