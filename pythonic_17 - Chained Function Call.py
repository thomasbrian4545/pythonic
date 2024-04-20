def tambah(a,b):
    return a+b

def kurang(a,b):
    return a-b

# Cara lama
kondisi = True
x,y = 100,50

if kondisi:
    hasil = tambah(x,y)
else:
    hasil = kurang(x,y)
print(hasil)

# Cara baru
hasil = (tambah if kondisi else kurang)(x,y)
print(hasil)