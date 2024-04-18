# Fungsi zip pada perulangan for loop

nim = ['111', '222', '333']
nama = ['anis', 'prabowo', 'ganjar']
hobi = ['mancing', 'makan', 'minum']

for d_nim, d_nama, d_hobi in zip(nim, nama, hobi) :
    print(f"{d_nim} --- {d_nama} --- {d_hobi}")