# Cara lama
fileku = open('pesan.txt', 'w')
fileku.write("Ayo belajar python\n")
fileku.write("di rumah Brian.")
fileku.close()

# Cara baru
with open('kabar.txt', 'w') as filemu:
    filemu.write("Ayo pergi ke Surabaya\n")
    filemu.write("naik mobil.\n")