listku = [20, 10, 40, 40, 70, 50, 60, 80]
hitung = 40

# Cara lama
""" jumlah = 0
for item in listku:
    if item == hitung:
        jumlah += 1
 """
# Cara baru
jumlah = listku.count(hitung)

print(f"Nilai {hitung} di dalam {listku} sebanyak {jumlah}")