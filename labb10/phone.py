import psycopg2
import csv

def menu():
    print("\nPhoneBook Menu:")
    print("1. Insert Data from CSV")
    print("2. Insert Data via Console")
    print("3. Update Data")
    print("4. Query Data")
    print("5. Delete Data")
    print("6. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            insert_from_csv()
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_data()
        elif choice == "4":
            query_data()
        elif choice == "5":
            delete_data()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")



try:
    conn = psycopg2.connect(
        dbname="phonebook",     # Replace with your real database name
        user="postgres",        # Replace with your username
        password="your_password",  # Replace with your real password
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    # Now you can safely use cursor to execute SQL commands
    print("Connected to the database successfully!")

except psycopg2.Error as e:
    print("Failed to connect to the database.")
    print("Error:", e)


def insert_from_csv():


# Connect to your PostgreSQL database
    conn = psycopg2.connect(
        dbname="phonebook", user="postgres", password="1234", host="localhost", port="5432"
)
cursor = conn.cursor()

# Open the CSV file and insert data
with open('phonebook.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header if it exists
    for row in csv_reader:
        cursor.execute(
    """
    INSERT INTO phonebook (first_name, last_name, phone)
    VALUES (%s, %s, %s)
    ON CONFLICT (phone) DO UPDATE
    SET first_name = EXCLUDED.first_name, last_name = EXCLUDED.last_name
    """,
    (row[0], row[1], row[2])
)

    conn.commit()

cursor.close()
conn.close()


def insert_from_console():
    import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="phonebook", user="postgres", password="1234", host="localhost", port="5432"
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


def update_data():
    import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="phonebook", user="postgres", password="1234", host="localhost", port="5432"
)
cursor = conn.cursor()

# Ask user for which record to update
phone = input("Enter the phone number of the person you want to update: ")

# Ask which field to update
choice = input("Do you want to update the first name or phone number? ")

if choice.lower() == "first name":
    new_first_name = input("Enter the new first name: ")
    cursor.execute(
        "UPDATE phonebook SET first_name = %s WHERE phone = %s",
        (new_first_name, phone)
    )
elif choice.lower() == "phone number":
    new_phone = input("Enter the new phone number: ")
    cursor.execute(
        "UPDATE phonebook SET phone = %s WHERE phone = %s",
        (new_phone, phone)
    )

conn.commit()
cursor.close()
conn.close()


def query_data():
    import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="phonebook", user="postgres", password="1234", host="localhost", port="5432"
)
cursor = conn.cursor()

# Query by name
first_name = input("Enter first name to search: ")
cursor.execute("SELECT * FROM phonebook WHERE first_name = %s", (first_name,))
rows = cursor.fetchall()

# Display results
for row in rows:
    print(f"{row[1]} {row[2]}: {row[3]}")

cursor.close()
conn.close()


def delete_data():
    import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="phonebook", user="postgres", password="1234", host="localhost", port="5432"
)
cursor = conn.cursor()

# Ask user for phone number to delete
phone = input("Enter the phone number to delete: ")

cursor.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))

conn.commit()
cursor.close()
conn.close()


if __name__ == "__main__":
    main()
