from sklearn.feature_extraction.text import TfidfVectorizer  

# Baca file teks  
with open('corpus.txt', 'r') as file:  
    corpus = file.readlines()  

# Inisialisasi TfidfVectorizer  
vect = TfidfVectorizer(stop_words='english')  

# Pembobotan TF-IDF  
resp = vect.fit_transform(corpus)  

# Cetak hasil  
print('Hasil TF-IDF with array:')  
print(resp.toarray())  
print('Hasil TF-IDF non array:')  
print(resp)  
print('Daftar Kata:')  
print(vect.get_feature_names_out())