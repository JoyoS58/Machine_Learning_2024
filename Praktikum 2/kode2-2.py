import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

data = 'Titanic-Dataset-fixed.csv' # path dataset
df = pd.read_csv(data) # load dataset
df.head()

df = df[['Survived', 'Pclass', 'Age', 'Sex', 'Cabin']]
df.head()

# import dataframe_image as dfi
# dfi.export(df.head(), 'slice_featarue.png')

le = LabelEncoder() # membuat objek dari LabelEncoder
df['Sex'] = le.fit_transform(df['Sex']) # proses encoding
df['Cabin'] = le.fit_transform(df['Cabin']) # proses encoding
df.head()

std = StandardScaler()
df['Age'] = std.fit_transform(df[['Age']])
df.head()