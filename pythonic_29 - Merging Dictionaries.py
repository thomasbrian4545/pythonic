data1 = {'nama' : 'Thomas Brian', 'usia' : 33}
data2 = {'kota' : 'Sidoarjo', 'ipk' : 3.67}

# Cara lama
mahasiswa = {}
for _ in data1:
    mahasiswa[_] = data1[_]
for _ in data2:
    mahasiswa[_] = data2[_]
print(mahasiswa)

# Cara baru
mahasiswa = {**data1, **data2}
print(mahasiswa)