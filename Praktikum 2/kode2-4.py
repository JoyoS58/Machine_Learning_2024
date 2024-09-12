from PIL import Image
 
img = Image.open('image.png')
img.show() # tampilkan gambar
display(img) # metode alternatif tampilkan gambar

# Ekstrak setiap channel red, green, blue
r, g, b = img.split()

# Cek panjang ukuran channel red
print(len(r.histogram()))

# Cetak fitur histogram pada channel red
print(r.histogram())