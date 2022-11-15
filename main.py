import generateData
import InitDatabase
import printData
import toSvd
from scipy.sparse import csr_matrix
 
  
if __name__ == '__main__':
    InitDatabase.createTable()
    generateData.insertIntoDB()
    df = printData.printData("Select * from data", InitDatabase.cnx)
    print(df)
    pt_df = df.pivot_table(
        columns = 'product_id',
        index = 'user_id',
        values = 'product_rating'
    ).fillna(0)

    mat = pt_df.values
    mat = csr_matrix(mat)
    
    pred_df = toSvd.generate_prediction_df(mat, pt_df, 10)

    print(toSvd.recommend_items(pred_df, 5, 10, 'users with same interests'))
    InitDatabase.dropTable()