import tkinter
import mysql.connector


mydb ={
  "host":"localhost",
  "user":"username",
  "password":"password",
}
connection = mysql.connector.connect(**mydb)
cursor = connection.cursor()

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
    mydb["database"]="my_expenses"
    #print(mydb)
    cursor.execute("USE my_expenses")
    print("Checking For Required Table : ")

    def check_table_exists_describe(table_name):
        try:
            sql = f"DESCRIBE {table_name}"
            cursor.execute(sql)
            print("It's there")
            return True  # If no error occurs, assume the table exists
        except mysql.connector.Error as err:
            # Check for specific error code indicating table not found (may vary)
            if err.errno == 1146:  # Table doesn't exist error code (example)
                return False
            else:
                print(f"Database error: {err}")
                return False  # Consider this inconclusive
    if check_table_exists_describe("data") :
       print("its there")
    else:
       print("Its not there")
       cursor.execute("CREATE TABLE data (title VARCHAR(50), amount INT(10), timeStamp TIMESTAMP ) ")





else:
    print("Creating Database : my_expenses ")
    cursor.execute("CREATE DATABASE my_expenses")
    cursor.execute("CREATE TABLE data (title VARCHAR(50), amount INT(10), timeStamp TIMESTAMP ")
