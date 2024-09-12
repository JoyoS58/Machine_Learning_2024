import pandas as pd  
from sklearn.model_selection import train_test_split  
from sklearn.preprocessing import StandardScaler, LabelEncoder  

# Langkah 1: Membaca data  
# Diasumsikan data telah dimuat ke dalam DataFrame  
data = pd.read_csv('wbc.csv')  
data.info()