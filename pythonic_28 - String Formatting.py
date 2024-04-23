nama = 'thomas'
usia = 33
print('Nama saya ' + nama + ' usia saya ' + str(usia) + ' tahun')
print('Nama saya %s usia saya %d tahun' % (nama, usia))
print('Nama saya {} usia saya {} tahun' .format(nama, usia))
print('Nama saya {1} usia saya {0} tahun' .format(usia, nama))
print(f'Nama saya {nama} usia saya {usia} tahun')

mahasiswa = {
    'nama' : 'Brian',
    'usia' : 33,
    'ipk' : 3.67
}
print('Nama saya {nama} dan usia {usia}' .format(**mahasiswa))
