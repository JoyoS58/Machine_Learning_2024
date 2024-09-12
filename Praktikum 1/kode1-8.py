corpus = [  
    'the house had a tiny little mouse',  
    'the cat saw the mouse',  
    'the mouse ran away from the house',  
    'the cat finally ate the mouse',  
    'the end of the mouse story'  
]
from sklearn.feature_extraction.text import TfidfVectorizer  

# Inisialisasi objek TfidfVectorizer  
vect = TfidfVectorizer(stop_words='english')  

# Pembobotan TF-IDF  
resp = vect.fit_transform(corpus)  

# Cetak hasil  
print(resp)

