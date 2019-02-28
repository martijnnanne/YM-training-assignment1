import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

BASE_PATH = '~/Documents/training_assignment_2/'

df = pd.read_csv(BASE_PATH + 'results/train_df.csv')
print(df)
df = df.dropna()
print(df)

feature_cols = [col for col in df.columns if 'PREV_' in col] + [col for col in df.columns if 'EXT_' in col]
X = df.loc[:, feature_cols]
y = df.TARGET

print(X.shape)
print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

logreg = LogisticRegression()

logreg.fit(X_train, y_train)

y_scores = logreg.predict(X_test)

print('AUC score', roc_auc_score(y_test, y_scores))
