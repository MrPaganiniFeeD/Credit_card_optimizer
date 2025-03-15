import psycopg2
from psycopg2 import sql 


# connection = psycopg2.connect(database="main", user="postgres", password="changeme", host="localhost", port=5432)

# cursor = connection.cursor()

# cursor.execute("SELECT * from users;")

# # Fetch all rows from database
# record = cursor.fetchall()

# print("Data from Database:- ", record)

DB_HOST = "localhost"
DB_NAME = "main"
DB_USER = "postgres"
DB_PASSWORD = "changeme"
PORT = 5432

# Function to populate the users table
def populate_users_table(users_data):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=PORT,
        )
        cursor = conn.cursor()

        # Insert data into the users table
        for user in users_data:
            insert_query = sql.SQL(
                """
                INSERT INTO users (name, money, cashback_importance)
                VALUES (%s, %s, %s)
                """
            )
            cursor.execute(insert_query, (user["name"], user["money"], user["cashback_importance"]))

        # Commit the transaction
        conn.commit()
        print("Data successfully inserted into the users table!")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def show_users_tabe():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=PORT,
        )
        cursor = conn.cursor()


        cursor.execute("SELECT * from users;")

        # Fetch all rows from database
        record = cursor.fetchall()

        print("Data from Database:\n", record)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    # Sample data to insert into the users table
    users_data = [
        {"name": "Ivan", "money": 100, "cashback_importance": 0},
        {"name": "Egor", "money": 200, "cashback_importance": 2},
        {"name": "Gleb", "money": 150, "cashback_importance": 5},
    ]

    # populate_users_table(users_data)

    show_users_tabe()