nim = ['100', '200', '300']
nama = ['Andi', 'Budi', 'Cici']
ipk = [3.25, 3.00, 3.50]

# Cara lama
mahasiswa = []
for _ in range(len(nim)):
    mahasiswa.append((nim[_], nama[_], ipk[_]))
print(f"Isi mahasiswa : {mahasiswa}")

# Cara baru
student = list(zip(nim, nama, ipk))
print(f"Isi student : {student}")