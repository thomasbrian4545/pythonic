mahasiswa = [
    ('100', 'Andi', 10000),
    ('200', 'Budi', 20000),
    ('300', 'Cici', 30000)
]

# Cara lama
""" nim = []
nama = []
uang = []
for item in mahasiswa:
    nim.append(item[0])
    nama.append(item[1])
    uang.append(item[2])
 """

# Cara baru
nim, nama, uang = zip(*mahasiswa)

print(f"Isi dari nim : {nim}")
print(f"Isi dari nama : {nama}")
print(f"Isi dari uang : {uang}")