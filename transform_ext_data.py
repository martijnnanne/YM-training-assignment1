import pandas as pd
import os
print(os.getcwd())
BASE_PATH = '~/Documents/training_assignment_2/'
ext_df = pd.read_csv(BASE_PATH + 'data_assignment2/external_data.csv')
ext_agg = ext_df.groupby('SK_ID_CURR').agg({
    'AMT_CREDIT_SUM': ['min', 'max', 'mean', 'sum']
})
ext_agg.columns = pd.Index(['EXT_' + e[0] + "_" + e[1].upper() for e in ext_agg.columns.tolist()])
ext_agg.to_csv(BASE_PATH + 'results/ext_transformed.csv')
