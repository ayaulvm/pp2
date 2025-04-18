import psycopg2
import json

# Database connection setup
def connect_db():
    return psycopg2.connect(
        dbname="phonebook",  
        user="postgres",     
        password="1234",  
        host="localhost",
        port="5432"
    )

# 1. Search records based on a pattern (name, surname, phone)
def search_records(pattern):
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM search_records(%s)", (pattern,))
    records = cur.fetchall()
    
    for record in records:
        print(record)
    
    cur.close()
    conn.close()

# 2. Insert or update a user (name and phone)
def insert_or_update_user(first_name, last_name, phone):
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute("CALL insert_or_update_user(%s, %s, %s)", (first_name, last_name, phone))
    
    conn.commit()
    cur.close()
    conn.close()

# 3. Insert multiple users, check phone validity
def insert_multiple_users(users_list):
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute("CALL insert_multiple_users(%s)", (users_list,))
    
    conn.commit()
    cur.close()
    conn.close()

# 4. Paginate query results from phonebook (limit and offset)
def get_paginated_data(limit_count, offset_count):
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM get_paginated_data(%s, %s)", (limit_count, offset_count))
    records = cur.fetchall()
    
    for record in records:
        print(record)
    
    cur.close()
    conn.close()

# 5. Delete user by username or phone
def delete_user(identifier):
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute("CALL delete_user_by_username_or_phone(%s)", (identifier,))
    
    conn.commit()
    cur.close()
    conn.close()

