import sqlite3


def create_connection(data_file):
    conn = None
    try:
        conn = sqlite3.connect(data_file)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        curses = conn.cursor()
        curses.execute(sql)
    except sqlite3.Error as e:
        print(e)


def create_product(conn, product):
    try:
        sql = '''INSERT INTO products 
        (product_title, price, quantity)
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product,)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


# 8. Добавить функцию, которая меняет количество товара по id
def update_product_quantity(conn, product):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product,)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


# 9. Добавить функцию, которая меняет цену товара по id
def update_product_price(conn, product):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product,)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


# 10. Добавить функцию, которая удаляет товар по id
def delete_product(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


# 11. Добавить функцию, которая бы выбирала все товары из БД и распечатывала бы их в консоли
def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


# 12. Добавить функцию, которая бы выбирала из БД
#     товары которые дешевле 100 сомов и количество которых больше чем 5 и распечатывала бы их в консоли
def select_products_by_price(conn):
    try:
        sql = '''SELECT * FROM products WHERE price < 100.0 AND quantity > 5'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def order_by_product(conn):
    try:
        sql = '''SELECT * FROM products order by price'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def find_product_word(conn, product):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE  ?'''
        cursor = conn.cursor()
        cursor.execute(sql, ('%_'+product+'%',))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


database = r'hw-24-2.db'
sql_creat_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER(5) NOT NULL DEFAULT 0
)
'''

connection = create_connection(database)
if connection is not None:
    print('Connected successfully')

    # create_table(connection, sql_creat_products_table)
    # create_product(connection, ('Хлопковое масло', 95.50, 100))
    # create_product(connection, ('Сахар', 56.50, 250)),
    # create_product(connection, ('Мыло', 15.00, 100)),
    # create_product(connection, ('Рыба', 450.45, 50)),
    # create_product(connection, ('Жидкое мыло', 50.50, 80)),
    # create_product(connection, ('Мыло Детское', 65.78, 95)),
    # create_product(connection, ('Шампунь', 120.37, 50)),
    # create_product(connection, ('Масло подсолничное', 125.00, 45)),
    # create_product(connection, ('Масло сливочное', 75.00, 70)),
    # create_product(connection, ('Картошка', 22.50, 250)),
    # create_product(connection, ('Лук', 15.75, 350)),
    # create_product(connection, ('Рис', 95.50, 460)),
    # create_product(connection, ('Макароны', 45.00, 200)),
    # create_product(connection, ('Шампунь детский', 180.50, 50)),
    # create_product(connection, ('Курица', 180.50, 85)),
    # create_product(connection, ('Окорочка', 200.35, 125)),
    # select_all_products(connection)
    # select_products_by_price(connection)
    # update_product_quantity(connection, (245, 1))
    # update_product_price(connection, (435, 3))
    # delete_product(connection, 17)
    find_product_word(connection, ('асло'))
    find_product_word(connection, ('ыло'))
    # order_by_product(connection)
    connection.close()
