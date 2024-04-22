listku = [10, 20, 30, 40, 50]
cari = 10

# Cara lama
hasil = False

for item in listku:
    if cari == item:
        hasil = True
        break

if hasil:
    print('Ditemukan')
else:
    print('Tidak Ditemukan')

# Cara baru
if cari in listku:
    print('Ditemukan')
else:
    print('Tidak Ditemukan')