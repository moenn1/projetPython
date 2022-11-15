
import pandas as pd
import numpy as np
import InitDatabase

from scipy.sparse import csr_matrix
from scipy.sparse.linalg import svds

def normalize(pred_ratings):
    return (pred_ratings - pred_ratings.min()) / (pred_ratings.max() - pred_ratings.min())
  
def generate_prediction_df(mat, pt_df, n_factors):
    if not 1 <= n_factors < min(mat.shape):
        raise ValueError("Must be 1 <= n_factors < min(mat.shape)")
        
    u, s, v = svds(mat, k = n_factors)
    s = np.diag(s)

    pred_ratings = np.dot(np.dot(u, s), v) 
    pred_ratings = normalize(pred_ratings)
    
    pred_df = pd.DataFrame(
        pred_ratings,
        columns = pt_df.columns,
        index = list(pt_df.index)
    ).transpose()
    return pred_df

def recommend_items(pred_df, usr_id, n_recs, name):
    usr_pred = pred_df[usr_id].sort_values(ascending = False).reset_index().rename(columns = {usr_id : name})
    rec_df = usr_pred.sort_values(by = name, ascending = False).head(n_recs)
    return rec_df

