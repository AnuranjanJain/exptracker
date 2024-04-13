from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt
import matplotlib.dates as mdates  # Import for date formatting
from tkinter import messagebox

import mysql.connector


mydb ={
  "host":"localhost",
  "user":"username",
  "password":"password",
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

#gui dev 

def update_expenses_list():
    try:
        expenses_listbox.delete(0, tk.END)  # Clear listbox
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()
        for expense in expenses:
            formatted_string = f"{expense[0]} - {expense[1]} - ${expense[2]} - {expense[3]}"
            expenses_listbox.insert(tk.END, formatted_string)
    except mysql.connector.Error as err:
        print(f"Error retrieving expense data: {err}")

def add_expense():
    try:
        title = title_entry.get()
        amount = float(amount_entry.get())
        timestamp = timestamp_entry.get()
        cursor.execute("INSERT INTO expenses (title, amount, timestamp) VALUES (%s, %s, %s)",
                       (title, amount, timestamp))
        connection.commit()
        messagebox.showinfo("Success", "Expense added successfully")
        update_expenses_list()
        plot_spending_insights()
    except (ValueError, mysql.connector.Error) as err:
        print(f"Error adding expense: {err}")
        messagebox.showerror("Error", f"Failed to add expense: {err}")
