import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="your_db_name", user="your_user", password="your_password", host="localhost", port="5432"
)
cursor = conn.cursor()

# Ask user for input
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
phone = input("Enter phone number: ")

# Insert data into the table
cursor.execute(
    "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)",
    (first_name, last_name, phone)
)

conn.commit()
cursor.close()
conn.close()
