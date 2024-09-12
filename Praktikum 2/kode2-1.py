import pandas as pd

data = 'Titanic-Dataset.csv' # path dataset
df = pd.read_csv(data) # load dataset

# Tampilkan data teratas
df.head()

# mengetahui jumlah data untuk setiap kolom.
df.info()

# jumlah data yang hilang untuk setiap kolom,
df.isnull().sum()

# Age - mean
df['Age'].fillna(value=df['Age'].mean(), inplace=True)

# Cabin - "DECK"
df['Cabin'].fillna(value="DECK", inplace=True)

# Embarked - modus
df['Embarked'].fillna(value=df['Embarked'].mode, inplace=True)

df.isnull().sum()

df.head(10)

