import pandas as pd
import InitDatabase

def printData(query, cnx):
    cursor = cnx.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    df = pd.DataFrame(result, columns = ['product_id', 'manufacturer_id', 'product_genre', 'user_id', 'weight', 'product_rating', 'ship_id', 'manufacture_year', 'product_price', 'text_lang'])
    return df


# df = printData("Select * from data", InitDatabase.cnx)
