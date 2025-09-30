import psycopg2

def create_table():
    # Connect to the PostgreSQL database
    connect = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="kiki",
        host="localhost",
        port="5432"
    )

    cursor = connect.cursor()
    cursor.execute("CREATE TABLE employees(Name text, ID int, Age int);")
    connect.commit()
    cursor.close()
    connect.close()
    print("Table created successfully.")
    
# Insert data into the table by taking user input
def insert_data():
    connect = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="kiki",
        host="localhost",
        port="5432"
    )

    name = input("Enter employee name: ")
    id = int(input("Enter employee ID: "))
    age = int(input("Enter employee age: "))
    cursor = connect.cursor()
    cursor.execute("INSERT INTO employees(Name, ID, Age) VALUES(%s, %s, %s);", (name, id, age))
    connect.commit()
    cursor.close()
    connect.close()
    print("Data added to table employee successfully.")
    
def execute_query(query):
        connect = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="kiki",
        host="localhost",
        port="5432"
    )

        cursor = connect.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        connect.commit()
        cursor.close()
        connect.close()
        print("Data extracted from employee successfully.")


if __name__ == "__main__":
    create_table()
    insert_data()
    query = "SELECT * FROM employees;"
    execute_query(query)

