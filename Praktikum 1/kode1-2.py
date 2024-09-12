import numpy as np  
from sklearn.preprocessing import MinMaxScaler  

np.set_printoptions(precision=6)  # bulatkan 4 angka koma  
np.set_printoptions(suppress=True)  # hilangkan nilai e  

# Kita akan membentuk data  
# Hal ini dikarenakan, scikit-learn hanya menerima input  
# dalam bentuk n-dimensional array  
data = [  
    [100, 0.0001],  
    [50, 0.05],  
    [30, 0.003]  
]  

# Ubah ke bentuk numpy n-dimensional array  
data = np.asarray(data)  
print('Data Asli')  
print(data)  

# Mendefinisikan obyek MinMaxScaler  
scaler = MinMaxScaler()  
# Transformasikan data  
scaled = scaler.fit_transform(data)  
print('Data Normalisasi')  
print(scaled)