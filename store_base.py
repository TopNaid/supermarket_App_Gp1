import psycopg2


def look(query):

    connection = psycopg2.connect(
            dbname = 'postgres',
            user = 'postgres',
            password = '12345678',
            host = 'localhost',
            port= '5050'
    )

    cursor = connection.cursor()

    cursor.execute("SELECT product, price FROM product WHERE product ILIKE %s", ('%' + query + '%',))

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results


def find_price(product):

    connection = psycopg2.connect(
            dbname = 'postgres',
            user = 'postgres',
            password = '12345678',
            host = 'localhost',
            port= '5050'
    )

    cursor = connection.cursor()

    cursor.execute("SELECT price FROM product WHERE product= %s", (product,))
    price = cursor.fetchall()

    cursor.close()
    connection.close()

    return price[0][0] if price else None