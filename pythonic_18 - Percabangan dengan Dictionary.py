def one():
    print("one-satu")
def two():
    print("two-dua")
def three():
    print("three-tiga")
kondisi = 'tiga'

# Cara lama
if kondisi == 'satu':
    one()
elif kondisi == 'dua':
    two()
elif kondisi == 'tiga':
    three()

# Cara baru
hasil = {
    'satu': one,
    'dua': two,
    'tiga': three 
}
hasil[kondisi]()