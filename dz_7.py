import sqlite3


def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return connection

def create_table(connection, create_table_sql):
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_product(connection, product):
    sql = '''INSERT INTO products(product_title, price, quantity) VALUES (?, ?, ?) '''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_product_by_quantity(db_file, product):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_product_by_price(db_file, product):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
    except sqlite3.Error as e:
        print(e)


def delete_product_by_id(db_file, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            connection.commit()
    except sqlite3.Error as e:
        print(e)


sql_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

def select_all_products(db_file):
    sql = '''SELECT * FROM products'''
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_by_cheaper_and_quantity(db_file, price, quantity):
    sql = '''SELECT * FROM products WHERE price < ? and quantity > ?'''
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (price, quantity))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_by_name(db_file):
    sql = '''SELECT * FROM products WHERE product_title LIKE '%мыло%' or 'мыло%' or '%мыло' '''
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

db_name = 'hw.db'
my_connection = create_connection(db_name)
if my_connection is not None:
    print('Successfully connected to database')
    # # create_table(my_connection, sql_create_products_table)
    # insert_product(my_connection,("Лампа настольная", 15.99, 100))
    # insert_product(my_connection,("Стул офисный", 89.99, 50))
    # insert_product(my_connection,("Детское мыло", 24.49, 70))
    # insert_product(my_connection, ("Телефон смартфон", 399.99, 30))
    # insert_product(my_connection, ("Шоколад молочный", 2.49, 300))
    # insert_product(my_connection, ("Пылесос ручной", 79.99, 40))
    # insert_product(my_connection, ("Ручка гелевая", 0.99, 500))
    # insert_product(my_connection, ("Гряное мыло", 3.99, 200))
    # insert_product(my_connection, ("Набор отверток", 12.99, 100))
    # insert_product(my_connection, ("Кофеварка капсульная", 149.99, 25))
    # insert_product(my_connection, ("Микроволновая печь", 199.99, 15),)
    # insert_product(my_connection, ("Гитара акустическая", 129.99, 10),)
    # insert_product(my_connection, ("Набор посуды", 495.99, 35))
    # insert_product(my_connection, ("мыло для лицо", 14.99, 80))
    # insert_product(my_connection, ("Сканер для документов", 89.99, 2))
    my_connection.close()


update_product_by_quantity(db_name, (81, 11))
update_product_by_price(db_name, (77.0, 3))
delete_product_by_id(db_name, 7)
select_all_products(db_name)
select_products_by_cheaper_and_quantity(db_name, 100, 5)
select_products_by_name(db_name)
