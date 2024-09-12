from sklearn.preprocessing import OneHotEncoder  

# Inisiasi objek OneHot Encoder  
de = OneHotEncoder(drop='first')  

# Definisikan data  
# dalam bentuk 2d  
data = [  
    ['Politeknik Negeri Malang'],  
    ['Politeknik Elektronika Negeri Surabaya'],  
    ['Politeknik Negeri Jakarta'],  
    ['Politeknik Negeri Semarang']  
]  

# Transformasi OneHot Encoder  
transform_de = de.fit_transform(data)  

print('Data Asli')  
print(data)  
print('Data Transformasi One-Hot Encoding')  
print(transform_de.toarray())