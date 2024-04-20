nama = ['brian', 'dewi', 'ava']
umur = [33, 32, 1]

listku = []
for i in range(len(nama)) :
    listku.append([nama[i], umur[i]])
print(f"listku : {listku}")

listmu = [[d_nama, d_umur] for d_nama, d_umur in zip(nama, umur)]
print(f"listmu : {listmu}")