import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish the connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='alfred1',            
            password='1234567890'     
        )
        
        if connection.is_connected():
            # Create a cursor object to execute SQL commands
            mycursor = connection.cursor()
            
            # Create database if it doesn't already exist
            mycursor.execute("CREATE DATABASE IF NOT EXISTS `alx_book_store`")
            print("Database 'alx_book_store' created successfully!")
    
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        # Close the cursor and connection if they were opened
        if 'mycursor' in locals():  
            mycursor.close()
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

# Call the function to create the database
create_database()
