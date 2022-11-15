import mysql.connector

cnx = mysql.connector.connect(
    host = 'localhost',
    user = 'root', 
    password = '',
    database = 'amazonDataset'
)   



cursor = cnx.cursor()

def createTable():
    cursor.execute("CREATE TABLE data(product_id int, manufacturer_id int, product_genre int, user_id int, weight int, product_rating int, ship_id int, manufacture_year int, product_price int, text_lang int);")
    cnx.commit()


def dropTable():
    cursor.execute("DROP TABLE data;")
    cnx.commit()