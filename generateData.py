import pandas as pd
import InitDatabase
from random import randint

def generate_data(n_products = 500, n_genres = 10, n_manufacturers = 50, n_ship = 20, n_users = 2000, dataset_size = 1000):
    d = pd.DataFrame(
        {
            'product_id' : [randint(1, n_products) for _ in range(dataset_size)],
            'manufacturer_id' : [randint(1, n_manufacturers) for _ in range(dataset_size)],
            'product_genre' : [randint(1, n_genres) for _ in range(dataset_size)],
            'user_id' : [randint(1, n_users) for _ in range(dataset_size)],
            'weight' : [randint(75, 700) for _ in range(dataset_size)],
            'product_rating' : [randint(1, 10) for _ in range(dataset_size)],
            'ship_id' : [randint(1, n_ship) for _ in range(dataset_size)],
            'manufacture_year' : [randint(2000, 2021) for _ in range(dataset_size)],
            'product_price' : [randint(1, 200) for _ in range(dataset_size)],
            'text_lang' : [randint(1,7) for _ in range(dataset_size)]
        }
    ).drop_duplicates()
    return d
  


    
def insertIntoDB():
    d = generate_data(dataset_size = 1000)
    cnx = InitDatabase.cnx
    cursor = InitDatabase.cursor
    for i in range(len(d)):
        cursor.execute("INSERT INTO data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", tuple(d.iloc[i]))
        cnx.commit()
    print("Data inserted successfully")
