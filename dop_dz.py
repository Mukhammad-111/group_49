import sqlite3


db_file = 'dop_dz.db'

def select_stores(db_name):
    sql = '''SELECT * FROM stores'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


def select_product_by_1(db_name):
    sql = '''SELECT p.title, p.category_code, p.unit_price, p.stock_quantity  
    FROM products as p WHERE id = 1'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


def select_product_by_2(db_name):
    sql = '''SELECT p.title, p.category_code, p.unit_price, p.stock_quantity  
    FROM products as p WHERE id = 2'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


def select_product_by_3(db_name):
    sql = '''SELECT p.title, p.category_code, p.unit_price, p.stock_quantity  
    FROM products as p WHERE id = 3'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)



is_true = True

while is_true:
    print("Вы можете отобразить список продуктов по выбранному id магазина из"
                    " перечня магазинов ниже")
    select_stores(db_file)
    show_id = int(input("Напишите id магазина или для выхода программ введите 0: "))
    if show_id == 0:
        break
    elif show_id == 1:
        select_product_by_1(db_file)
    elif show_id == 2:
        select_product_by_2(db_file)
    elif show_id == 3:
        select_product_by_3(db_file)
    else:
        print("Вы неправильно ввели")










