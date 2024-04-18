# Fungsi enumerate pada perulangan for loop

nim = ['001', '002', '003']
nama = ['anis', 'prabowo', 'ganjar']

for i in range(len(nim)) :
    print(f"nim = {nim[i]} --- nama = {nama[i]}")

for i, data_nim in enumerate(nim) :
    print(f"nim = {data_nim} --- nama = {nama[i]}")