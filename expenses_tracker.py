from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt
import matplotlib.dates as mdates  # Import for date formatting
from tkinter import messagebox

import mysql.connector


mydb ={
  "host":"localhost",
  "user":"root",
  "password":"6439",
}

try:
    connection = mysql.connector.connect(**mydb)
    cursor = connection.cursor(buffered=True)  # Use buffered cursor
except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")
    exit()

print("Connection Established \n ")
    
print("\n Checking Required Database Present or Not :) ")


def create_database_table():
    cursor.execute("CREATE DATABASE IF NOT EXISTS my_expenses")
    cursor.execute("USE my_expenses")
    cursor.execute("""CREATE TABLE IF NOT EXISTS expenses (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        title VARCHAR(255),
                        amount DECIMAL(10, 2),
                        timestamp DATETIME
                    )""")
    connection.commit()
create_database_table()
