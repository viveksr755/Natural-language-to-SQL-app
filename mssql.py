import pyodbc

# Define the connection string
connection_string = (
    "DRIVER={SQL Server};"
    "SERVER=PIC4556;"  # Use double backslashes to escape the backslash character
    "DATABASE=llm_app_data;"  # Remove the square brackets around the database name
    "Trusted_Connection=yes;"  # Use this if you are using Windows Authentication
     #"UID=pitsdba;"  # Uncomment and replace with your username if using SQL Server Authentication
     #"PWD=frontiers@2014;"  # Uncomment and replace with your password if using SQL Server Authentication
)

# Establish connection to the SQL Server database
connection = pyodbc.connect(connection_string)

# Creation of cursor
cursor = connection.cursor()

# Query to select data from the AttendanceData table
data = cursor.execute("SELECT * FROM AttendanceData")

# Fetch and print all rows from the query result
for row in data:
    print(row)

# Commit the transaction (not necessary in this case, but it's good practice to include it)
connection.commit()

# Close the connection
connection.close()  # Fixed the typo from "connection. Close()" to "connection.close()"




