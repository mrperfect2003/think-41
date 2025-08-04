import sqlite3
import pandas as pd
import os

# File check
if not os.path.exists('users.csv') or not os.path.exists('orders.csv'):
    print("❌ CSV files not found. Please ensure 'users.csv' and 'orders.csv' are in the same directory.")
    exit()

# Connect to SQLite
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Run schema.sql
with open('schema.sql', 'r') as f:
    cursor.executescript(f.read())

# Load users.csv
users_df = pd.read_csv('users.csv')
users_df.to_sql('users', conn, if_exists='append', index=False)

# Load orders.csv
orders_df = pd.read_csv('orders.csv')
orders_df.to_sql('orders', conn, if_exists='append', index=False)

# Verifying load
user_count = cursor.execute("SELECT COUNT(*) FROM users").fetchone()[0]
order_count = cursor.execute("SELECT COUNT(*) FROM orders").fetchone()[0]

print(f"✅ Loaded {user_count} users")
print(f"✅ Loaded {order_count} orders")

conn.commit()
conn.close()
