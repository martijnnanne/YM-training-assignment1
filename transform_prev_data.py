import pandas as pd


BASE_PATH = '~/Documents/training_assignment_2/'
prev_df = pd.read_csv(BASE_PATH + 'data_assignment2/prev_filtered.csv')
prev_agg = prev_df.groupby('SK_ID_CURR').agg({
    'AMT_CREDIT': ['min', 'max', 'mean', 'sum']
})
prev_agg.columns = pd.Index(['PREV_' + e[0] + "_" + e[1].upper() for e in prev_agg.columns.tolist()])
prev_agg.to_csv(BASE_PATH + 'results/prev_transformed.csv')