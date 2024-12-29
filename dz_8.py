import sqlite3



database_name = 'hw_8.db'

def select_cities(database_file):
    sql = '''SELECT c.citi_id, c.title FROM cities as c'''
    try:
        with sqlite3.connect(database_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


def select_info_city_by_id1(database_file):
    sql = '''SELECT st.first_name, st.last_name, cs.title, ci.title, ci.area FROM cities as ci 
    LEFT OUTER JOIN students as st ON st.city_id = ci.citi_id
    LEFT OUTER JOIN countries as cs ON cs.id = ci.country_id
    WHERE ci.citi_id = 1'''
    try:
        with sqlite3.connect(database_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


def select_info_city_by_id2(database_file):
    sql = '''SELECT st.first_name, st.last_name, cs.title, ci.title, ci.area FROM cities as ci
    LEFT JOIN students as st ON st.city_id = ci.citi_id
    LEFT JOIN countries as cs ON cs.id = ci.country_id
    WHERE ci.citi_id = 2'''
    try:
        with sqlite3.connect(database_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


def select_info_city_by_id3(database_file):
    sql = '''SELECT st.first_name, st.last_name, cs.title, ci.title, ci.area FROM cities as ci 
    LEFT JOIN students as st ON st.city_id = ci.citi_id
    LEFT JOIN countries as cs ON cs.id = ci.country_id
    WHERE ci.citi_id = 3'''
    try:
        with sqlite3.connect(database_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


def select_info_city_by_id4(database_file):
    sql = '''SELECT st.first_name, st.last_name, cs.title, ci.title, ci.area FROM cities as ci
    LEFT JOIN students as st ON st.city_id = ci.citi_id
    LEFT JOIN countries as cs ON cs.id = ci.country_id
    WHERE ci.citi_id = 4'''
    try:
        with sqlite3.connect(database_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


def select_info_city_by_id5(database_file):
    sql = '''SELECT st.first_name, st.last_name, cs.title, ci.title, ci.area FROM cities as ci
    LEFT JOIN students as st ON st.city_id = ci.citi_id
    LEFT JOIN countries as cs ON cs.id = ci.country_id
    WHERE ci.citi_id = 5'''
    try:
        with sqlite3.connect(database_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


def select_info_city_by_id6(database_file):
    sql = '''SELECT st.first_name, st.last_name, cs.title, ci.title, ci.area FROM cities as ci
    LEFT JOIN students as st ON st.city_id = ci.citi_id
    LEFT JOIN countries as cs ON cs.id = ci.country_id
    WHERE ci.citi_id = 6'''
    try:
        with sqlite3.connect(database_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


def select_info_city_by_id7(database_file):
    sql = '''SELECT st.first_name, st.last_name, cs.title, ci.title, ci.area FROM cities as ci
    LEFT JOIN students as st ON st.city_id = ci.citi_id
    LEFT JOIN countries as cs ON cs.id = ci.country_id
    WHERE ci.citi_id = 7'''
    try:
        with sqlite3.connect(database_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


while 1:
    try:
        print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже")
        select_cities(database_name)
        id_show = int(input('Введите id или для выхода из программы введите 0: '))
        if id_show == 0:
            print('Программа успешно завершился')
            break
        elif id_show == 1:
            select_info_city_by_id1(database_name)
        elif id_show == 2:
            select_info_city_by_id2(database_name)
        elif id_show == 3:
            select_info_city_by_id3(database_name)
        elif id_show == 4:
            select_info_city_by_id4(database_name)
        elif id_show == 5:
            select_info_city_by_id5(database_name)
        elif id_show == 6:
            select_info_city_by_id6(database_name)
        elif id_show == 7:
            select_info_city_by_id7(database_name)
        else:
            raise ValueError('Извините нет такой id')
    except ValueError as e:
        print(e)
