import tkinter
import mysql.connector


mydb ={
  "host":"localhost",
  "user":"Username", # write username here
  "password":"Password", # write passwoed here
}

def check_database_exists(db_name):
  try:
    connection = mysql.connector.connect(**mydb, database=db_name)
    connection.close()  # Close the connection even if successful
    return True
  except mysql.connector.Error as err:
    # Connection error likely means the database doesn't exist
    if err.errno == 1049:  # Database not found error code
      return False
    else:
      # Handle other potential errors here (e.g., permission issues)
      print(f"Database connection error: {err}")
      return False
    


print(" Checking Required Database Present or Not :) ")


if check_database_exists("my_expenses") : 
  print(" Already Exists , Means that you have already run this program before xD")






else:
  print("Creating Database : my_expenses ")
  mycursor = mydb.cursor()
  mycursor.execute("CREATE DATABASE my_expenses")
  mycursor.execute("CREATE TABLE data (title VARCHAR(50), amount INT(10), timeStamp TIMESTAMP ")
