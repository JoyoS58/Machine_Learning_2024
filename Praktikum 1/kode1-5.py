from sklearn.preprocessing import OneHotEncoder  

# Inisiasi objek OneHot Encoder  
ohe = OneHotEncoder()  

# Definisikan data  
# dalam bentuk 2d  
data = [  
    ['Politeknik Negeri Malang'],  
    ['Politeknik Elektronika Negeri Surabaya'],  
    ['Politeknik Negeri Jakarta'],  
    ['Politeknik Negeri Semarang']  
]  

# Transformasi OneHot Encoder  
transform_ohe = ohe.fit_transform(data)  

print('Data Asli')  
print(data)  

print('Data Transformasi One-Hot Encoding')  
print(transform_ohe.toarray())
