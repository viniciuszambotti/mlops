import pandas as pd
import numpy as np
import pickle



df_test = pd.read_csv('../data/test.csv')
df_train = pd.read_csv('../data/train.csv')

df = df_test.append(df_train)
# Transforma variaveis string em categórica
df[['god','type']] = df[['god','type']].astype("category")

df['cat_god'] = df['god'].cat.codes
df['cat_type'] = df['type'].cat.codes


with open('../data/data_prep_test.pkl', 'wb') as handle:
    pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)



