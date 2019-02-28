import pandas as pd

BASE_PATH = '~/Documents/training_assignment_2/'

prev_transformed_df = pd.read_csv(BASE_PATH + 'results/prev_transformed.csv')
ext_transformed_df = pd.read_csv(BASE_PATH + 'results/prev_transformed.csv')
fact_df = pd.read_csv(BASE_PATH + 'data_assignment2/train_fact.csv')

train_df = fact_df.join(prev_transformed_df.set_index('SK_ID_CURR'), how='left', on='SK_ID_CURR')
train_df = fact_df.join(ext_transformed_df.set_index('SK_ID_CURR'), how='left', on='SK_ID_CURR')
train_df.to_csv(BASE_PATH + 'results/train_df.csv', index=False)